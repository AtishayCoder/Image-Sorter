import pathlib
import shutil
import os
from tkinter import filedialog

image_extensions = ["jpg", "jpeg", "jpe", "jif", "jfif", "jfi", "png", "webp", "tiff", "tif", "raw", "arw", "cr2", "nrw", "k25", "bmp", "dib", "heif", "heic", "svg", "svgz"]

# Get selected directory
dir = filedialog.askdirectory()

# Segregate according folder or file
dirs = os.listdir(dir)
print(dirs)

if dirs != []:
    try: 
        os.makedirs(f"{dir}/Folders")
    except FileExistsError:
        pass
    for d in dirs:
        if os.path.isdir(f"{dir}/{d}"):
            shutil.move(f"{dir}/{d}", f"{dir}/Folders")
    # Segregate files
    files = (file for file in os.listdir(dir) 
         if os.path.isfile(os.path.join(dir, file)))
    try:
        os.makedirs(f"{dir}/Files")
    except FileExistsError:
        pass
    for f in files:
        shutil.move(f"{dir}/{f}", f"{dir}/Files/{f}")
