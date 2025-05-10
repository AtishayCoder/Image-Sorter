import os
import sorter.subject_identifier as subject_identifier
import sorter.extension_sorter as extension_sorter

def invoker(dir):
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