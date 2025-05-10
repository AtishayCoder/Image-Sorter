import os

def sort_by_extension(base_folder_path):
    # Get list of files
    files = [i for i in os.listdir(base_folder_path) if os.path.isfile(os.path.join(base_folder_path, i))]
    
    # Get extensions
    extensions = []
    for f in files:
        ext = f.split(".")[1]
        extensions.append(ext.upper())
        pass