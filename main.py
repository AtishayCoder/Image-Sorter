# import shutil
# import os
# from tkinter import filedialog

# image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".webp", ".tiff", ".tif", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".svg", ".svgz"]

# # Get selected directory
# dir = filedialog.askdirectory()

# # Segregate according folder or file
# dirs = os.listdir(dir)

# if dirs != []:
#     try: 
#         os.makedirs(os.path.join(dir, "Folders"))
#     except FileExistsError:
#         pass
#     for d in dirs:
#         if os.path.isdir(os.path.join(dir, d)):
#             shutil.move(os.path.join(dir, d), os.path.join(dir, "Folders"))
#     # Segregate files
#     files = (file for file in os.listdir(dir) 
#          if os.path.isfile(os.path.join(dir, file)))
#     try:
#         os.makedirs(os.path.join(dir, "Files"))
#     except FileExistsError:
#         pass
#     for f in files:
#         shutil.move(os.path.join(dir, f), os.path.join(dir, os.path.join("Files", f)))
        

# # Segregate pictures and other documents
# image_files_found = False
# files_to_move = []

# # Check if there are image files
# for item in os.listdir(os.path.join(dir, "Files")):
#   item_path = os.path.join(dir, "Files", item)
#   if os.path.isfile(item_path):
#     _, file_extension = os.path.splitext(item)
#     print(file_extension)
#     if file_extension.lower() in [ext.lower() for ext in image_extensions]:
#       image_files_found = True
#       files_to_move.append(item)

# if image_files_found:
#   images_folder = os.path.join(dir, os.path.join("Files", "Images"))
#   if not os.path.exists(images_folder):
#     os.makedirs(images_folder)
#     print(f"Created 'images' folder in '{dir}'.")
#   else:
#     print(f"'images' folder already exists in '{dir}'.")

#   for file_name in files_to_move:
#     source_path = os.path.join(dir, "Files", file_name)
#     destination_path = os.path.join(images_folder, file_name)
#     try:
#       shutil.move(source_path, destination_path)
#       print(f"Moved '{file_name}' to '{images_folder}'.")
#     except Exception as e:
#       print(f"Error moving '{file_name}': {e}")
# else:
#   print(f"No files with extensions found.")


import shutil
import os
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
    print("No other files found in '{os.path.join(dir, 'Files')}'.")