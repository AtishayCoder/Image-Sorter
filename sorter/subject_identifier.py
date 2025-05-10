import cv2
import os
import shutil
from PIL import Image
import numpy as np

face_cascade = None
output_folders = None

def filter_overlapping_faces(faces, overlapThresh=0.3):
    if len(faces) == 0:
        return []

    boxes = []
    for (x, y, w, h) in faces:
        boxes.append([x, y, x + w, y + h])

    boxes = np.array(boxes)
    pick = cv2.dnn.NMSBoxes(
        boxes.tolist(),
        [1.0] * len(boxes),
        score_threshold=0.0,
        nms_threshold=overlapThresh
    )

    if len(pick) == 0:
        return []

    pick = pick.flatten()
    return [faces[i] for i in pick]

def try_rotate_and_detect(img_path):
    detected_angle = None

    for angle in range(1, 360):
        pil_img = Image.open(img_path)
        rotated_pil = pil_img.rotate(angle, expand=True, fillcolor=(0, 0, 0))

        rotated_cv = cv2.cvtColor(np.array(rotated_pil), cv2.COLOR_RGB2BGR)
        gray_rotated = cv2.cvtColor(rotated_cv, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_rotated, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        faces = [face for face in faces if face[2] > 50 and face[3] > 50]
        faces = filter_overlapping_faces(faces)

        if len(faces) > 0:
            print(f"Detected face after rotating {angle} degrees.")
            detected_angle = angle
            break

    if detected_angle is not None:
        nearest_angle = min([0, 90, 180, 270], key=lambda x: abs(x - detected_angle))
        print(f"Saving corrected rotation. Nearest angle chosen: {nearest_angle} degrees.")

        pil_img = Image.open(img_path)
        final_rotated = pil_img.rotate(nearest_angle, expand=True, fillcolor=(0, 0, 0))
        final_rotated.save(img_path)

        img_cv = cv2.imread(img_path)
        if img_cv is None:
            print(f"Error reading corrected image {img_path}")
            return 0

        gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        faces = [face for face in faces if face[2] > 50 and face[3] > 50]
        faces = filter_overlapping_faces(faces)

        num_faces = len(faces)
        print(f"Detected {num_faces} face(s) after final correction.")

        return num_faces

    return 0

def handle_image(filename, input_folder):
    img_path = os.path.join(input_folder, filename)

    print(f"Handling file: {img_path}")

    if not os.path.isfile(img_path):
        print(f"Skipping {img_path}, not a file.")
        return

    try:
        img = cv2.imread(img_path)
        if img is None:
            print(f"Warning: Could not read image {filename}. Skipping.")
            return

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        faces = [face for face in faces if face[2] > 50 and face[3] > 50]
        faces = filter_overlapping_faces(faces)

        num_faces = len(faces)
        print(f"Initial detection found {num_faces} face(s)")

        # New logic: If multiple faces but 1 large face (likely portrait), count as 1
        if num_faces > 1:
            areas = [w * h for (x, y, w, h) in faces]
            max_area = max(areas)
            large_faces = [area for area in areas if area > 0.5 * max_area]
            if len(large_faces) == 1:
                print("Multiple detections but one large face found - treating as single face.")
                num_faces = 1

        if num_faces == 0:
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
    print(f"Input folder: {input_folder}")

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    output_folders = {
        'Me': os.path.join(input_folder, 'Me'),
        'Family': os.path.join(input_folder, 'Family'),
        'Nature': os.path.join(input_folder, 'Nature')
    }

    for name, folder in output_folders.items():
        os.makedirs(folder, exist_ok=True)
        print(f"Ensured folder exists: {folder}")

    for filename in os.listdir(input_folder):
        print("Processing " + filename)
        handle_image(filename=filename, input_folder=input_folder)
