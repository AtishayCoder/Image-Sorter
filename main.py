import cv2
import pathlib
import shutil
import os
from tkinter import filedialog

image_extensions = ["jpg", "jpeg", "jpe", "jif", "jfif", "jfi", "png", "webp", "tiff", "tif", "raw", "arw", "cr2", "nrw", "k25", "bmp", "dib", "heif", "heic", "svg", "svgz"]

# Get selected directory
dir = filedialog.askdirectory()

# Segregate according folder or file
dirs = os.walk(dir)
if dirs != []:
    os.makedirs(f"{dir}/Folders")
    for d in dirs:
        shutil.move(d, f"{dir}/Folders")
    # Segregate files
    files = (file for file in os.listdir(dir) 
         if os.path.isfile(os.path.join(dir, file)))
    os.makedirs(f"{dir}/Files")
    for f in files:
        shutil.move(f"{dir}/{f}", f"{dir}/Files/{f}")
