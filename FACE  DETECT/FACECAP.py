import tkinter as tk
from tkinter import filedialog
import cv2

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in an image
def detect_faces(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Function to open a file dialog and display the detected faces
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        faces = detect_faces(file_path)
        display_faces(file_path, faces)

# Function to display the detected faces
def display_faces(image_path, faces):
    image = cv2.imread(image_path)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Create the GUI
root = tk.Tk()
root.title("Face Detection")

browse_button = tk.Button(root, text="Browse Image", command=open_file)
browse_button.pack()

root.mainloop()
