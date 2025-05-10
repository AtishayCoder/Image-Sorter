import cv2
import os
import shutil
from PIL import Image
import numpy as np

face_cascade = None
output_folders = None

def try_rotate_and_detect(img_path):
    detected_angle = None

    # Step 1: Search for any face to fix rotation
    for angle in range(1, 360):
        pil_img = Image.open(img_path)
        rotated_pil = pil_img.rotate(1, expand=True)

        rotated_cv = cv2.cvtColor(np.array(rotated_pil), cv2.COLOR_RGB2BGR)
        gray_rotated = cv2.cvtColor(rotated_cv, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_rotated, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            print(f"Detected face after rotating {angle} degrees.")
            detected_angle = angle
            break

    if detected_angle is not None:
        # Step 2: Rotate to nearest normal angle
        nearest_angle = min([0, 90, 180, 270], key=lambda x: abs(x - detected_angle))
        print(f"Saving corrected rotation.")

        pil_img = Image.open(img_path)
        final_rotated = pil_img.rotate(nearest_angle, expand=True, fillcolor=(0, 0, 0))
        final_rotated.save(img_path)  # Overwrite original image

        # Step 3: Re-load corrected image and re-run face detection properly
        img_cv = cv2.imread(img_path)
        if img_cv is None:
            print(f"Error reading corrected image {img_path}")
            return 0  # No faces found because can't read

        gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        num_faces = len(faces)
        print(f"Detected {num_faces} face(s) after final correction.")

        return num_faces  # Return correct number of faces after proper detection

    return 0  # No faces detected after all rotation attempts


def handle_image(filename, input_folder):
    img_path = os.path.join(input_folder, filename)
    
    if not os.path.isfile(img_path):
        return

    try:
        img = cv2.imread(img_path)
        if img is None:
            print(f"Warning: Could not read image {filename}. Skipping.")
            return

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        num_faces = len(faces)

        if num_faces == 0:
            # No face detected initially — try rotation and fix angle
            num_faces = try_rotate_and_detect(img_path)

        source_path = img_path
        if num_faces == 1:
            destination_path = os.path.join(output_folders['Me'], filename)
            shutil.move(source_path, destination_path)
            print(f"Moved '{filename}' to 'Me' folder.")
        elif num_faces > 1:
            destination_path = os.path.join(output_folders['Family'], filename)
            shutil.move(source_path, destination_path)
            print(f"Moved '{filename}' to 'Family' folder.")
        else:
            destination_path = os.path.join(output_folders['Nature'], filename)
            shutil.move(source_path, destination_path)
            print(f"Moved '{filename}' to 'Nature' folder.")

    except Exception as e:
        print(f"Error processing {filename}: {e}")



def segregate_images(input_folder):
    global face_cascade, output_folders

    print("Invoked OpenCV handler.")

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    output_folders = {
        'Me': os.path.join(input_folder, 'Me'),
        'Family': os.path.join(input_folder, 'Family'),
        'Nature': os.path.join(input_folder, 'Nature')
    }

    for folder in output_folders.values():
        os.makedirs(folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        handle_image(filename=filename, input_folder=input_folder)
