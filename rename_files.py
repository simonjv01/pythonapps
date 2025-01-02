import os
import glob

# Set the folder path
folder_path = 'C:/Users/sjvar/OneDrive/Pictures/Running/'

# Get all the files in the folder
filenames = glob.glob(folder_path + '/*')

# Iterate over the files
for index, filename in enumerate(filenames):
    # Generate the new filename with a number appended
    base, extenstion = os.path.splitext(filename)
    name = "FirstonFirst5K"
    new_filename = f'{name}_{index + 1}{extenstion}'

    # Rename the file
    os.rename(filename, new_filename)
