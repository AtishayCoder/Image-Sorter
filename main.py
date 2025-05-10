import shutil
import os
import subject_identifier
import extension_sorter
from tkinter import filedialog

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".webp", ".tiff", ".tif", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".svg", ".svgz"]

# Get selected directory
dir = filedialog.askdirectory()

# Segregate according folder or file
dirs = os.listdir(dir)

if dirs != []:
    try:
        os.makedirs(os.path.join(dir, "Folders"))
    except FileExistsError:
        pass
    for d in dirs:
        if os.path.isdir(os.path.join(dir, d)):
            shutil.move(os.path.join(dir, d), os.path.join(dir, "Folders"))
    # Segregate files
    files = [file for file in os.listdir(dir)
             if os.path.isfile(os.path.join(dir, file))]
    try:
        os.makedirs(os.path.join(dir, "Files"))
    except FileExistsError:
        pass
    for f in files:
        shutil.move(os.path.join(dir, f), os.path.join(dir, os.path.join("Files", f)))


# Segregate pictures and other documents
image_files_found = False
other_files_found = False
files_to_move_images = []
files_to_move_others = []

# Check files in the "Files" directory
files_in_files = os.listdir(os.path.join(dir, "Files"))

for item in files_in_files:
    item_path = os.path.join(dir, "Files", item)
    if os.path.isfile(item_path):
        _, file_extension = os.path.splitext(item)
        if file_extension.lower() in [ext.lower() for ext in image_extensions]:
            image_files_found = True
            files_to_move_images.append(item)
        else:
            other_files_found = True
            files_to_move_others.append(item)

# Move image files
if image_files_found:
    images_folder = os.path.join(dir, os.path.join("Files", "Images"))
    if not os.path.exists(images_folder):
        os.makedirs(images_folder)
        print(f"Created 'Images' folder in '{os.path.join(dir, "Files")}'.")
    else:
        print(f"'Images' folder already exists in '{os.path.join(dir, "Files")}'.")

    for file_name in files_to_move_images:
        source_path = os.path.join(dir, "Files", file_name)
        destination_path = os.path.join(images_folder, file_name)
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved '{file_name}' to '{images_folder}'.")
        except Exception as e:
            print(f"Error moving '{file_name}' to '{images_folder}': {e}")
else:
    print(f"No image files found in '{os.path.join(dir, "Files")}'.")

# Move other files
if other_files_found:
    others_folder = os.path.join(dir, os.path.join("Files", "Others"))
    if not os.path.exists(others_folder):
        os.makedirs(others_folder)
        print(f"Created 'Others' folder in '{os.path.join(dir, "Files")}'.")
    else:
        print(f"'Others' folder already exists in '{os.path.join(dir, "Files")}'.")

    for file_name in files_to_move_others:
        source_path = os.path.join(dir, "Files", file_name)
        destination_path = os.path.join(others_folder, file_name)
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved '{file_name}' to '{others_folder}'.")
        except Exception as e:
            print(f"Error moving '{file_name}' to '{others_folder}': {e}")
else:
    print(f"No other files found in '{os.path.join(dir, 'Files')}'.")

# Check for 'Files' and 'Images' folder and invoke function
files_folder_path = os.path.join(dir, "Files")
images_folder_path = os.path.join(files_folder_path, "Images")
other_files_folder_path = os.path.join(files_folder_path, "Others")

if os.path.exists(files_folder_path) and os.path.isdir(files_folder_path):
    if os.path.exists(images_folder_path) and os.path.isdir(images_folder_path):
        subject_identifier.segregate_images(images_folder_path)
    else:
        print(f"The 'Images' folder was not found inside '{files_folder_path}'.")

    if os.path.exists(other_files_folder_path) and os.path.isdir(other_files_folder_path):
        print("'Others' folder found! Starting segregation.")
        extension_sorter.sort_by_extension(other_files_folder_path)
    else:
        print("No other files. Skipping sort by extension.")
else:
    print(f"The 'Files' folder was not found in the base directory '{dir}'.")