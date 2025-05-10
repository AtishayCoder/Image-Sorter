import os, shutil

def segregate_files_and_folders(dir):
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