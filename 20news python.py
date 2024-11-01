import os
import random

# Define paths to the train and test folders based on your provided paths
train_folder = r'C:\Users\PC\Downloads\20 Newsgroups Dataset\20news-bydate-train'
test_folder = r'C:\Users\PC\Downloads\20 Newsgroups Dataset\20news-bydate-test'

# List to store the concatenated text with boundary markers
segmented_text = []

# Loop through both the train and test folders
for main_folder in [train_folder, test_folder]:
    categories = os.listdir(main_folder)
    
    # Shuffle categories to create varied topic segments
    random.shuffle(categories)
    
    for category in categories:
        category_path = os.path.join(main_folder, category)
        
        # Check if it's a directory
        if os.path.isdir(category_path):
            files = os.listdir(category_path)
            random.shuffle(files)  # Shuffle files for randomness
            
            for file_name in files:
                file_path = os.path.join(category_path, file_name)
                
                # Read each file
                with open(file_path, 'r', encoding='latin-1') as f:
                    text = f.read().strip()
                    
                    # Add the text and a boundary marker
                    segmented_text.append(text)
                    segmented_text.append("===END===")  # Marker for segmentation boundary

# Join all segments into a single string with two newlines between segments
final_text = "\n\n".join(segmented_text)

# Specify the output path for the segmented file
output_path = r'C:\Users\PC\Downloads\20 Newsgroups Dataset\20news_segmented_data.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_text)

print(f"Preprocessing complete. Segmented file saved as '{output_path}'.")
