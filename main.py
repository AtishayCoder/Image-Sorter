from turtle import Screen
import cv2
import pathlib
import shutil


user_input = Screen().textinput("Enter path to folder", "Please enter the full "
                                                        "path to the folder with the images: ")


folder_items = []
number_of_faces_in_each_img = []


for filepath in pathlib.Path(user_input).glob('**/*'):
    folder_items.append(str(filepath.absolute()))

for item in folder_items:
    image = cv2.imread(item)
    gray_scale_img = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(image)
    number_of_faces_in_each_img.append(len(faces))

for i in range(0, len(number_of_faces_in_each_img)):
    if number_of_faces_in_each_img[i] == 1:
        shutil.move(folder_items[i], "me")

    if number_of_faces_in_each_img[i] > 1:
        shutil.move(folder_items[i], "family")

    if number_of_faces_in_each_img[i] < 1:
        shutil.move(folder_items[i], "nature and other")
