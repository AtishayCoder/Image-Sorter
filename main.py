import sorter.cv2_invoker as cv2_invoker
import sorter.file_folder_seg as file_folder_seg
import sorter.files_and_img_seg as files_and_images_seg
from tkinter import filedialog

# Get selected directory
dir = filedialog.askdirectory()

# Segregate according folder or file
file_folder_seg.segregate_files_and_folders(dir=dir)

# Segregate pictures and other documents
files_and_images_seg.segregate_images_and_docs(dir=dir)

# Check for 'Files' and 'Images' folder and invoke function
cv2_invoker.invoker(dir=dir)