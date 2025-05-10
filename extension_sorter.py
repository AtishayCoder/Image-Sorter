import os
import shutil

def sort_by_extension(base_folder_path):
    # Get list of files
    files = [i for i in os.listdir(base_folder_path) if os.path.isfile(os.path.join(base_folder_path, i))]
    
    # Get extensions
    extensions = []
    for f in files:
        ext = f.split(".")[1]
        if ext.upper() not in extensions:
            extensions.append(ext.upper())

    print(f"Extensions found: {extensions}")
    
    # Create folders
    for e in extensions:
        os.makedirs(os.path.join(base_folder_path, e))

    # Move files
    for f in files:
        ext = f.split(".")[1]
        shutil.move(os.path.join(base_folder_path, f), os.path.join(base_folder_path, ext.upper()))