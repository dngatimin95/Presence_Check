# Modified version of an example on facial recognition by ageitgey

import face_recognition
import cv2
import os
import numpy as np

capture = cv2.VideoCapture(0)
train_face_encodings = []
train_face_names = []
char_image_file = "C:\\Users\\Darren\\Documents\\GitHub\\Presence_Check\\charImages" # Insert file path to where you kept people's faces

for faces in os.listdir(char_image_file):
    char_image = face_recognition.load_image_file(os.path.join(char_image_file,faces))
    char_face_encoding = face_recognition.face_encodings(char_image)[0]

    train_face_encodings.append(char_face_encoding)
    train_face_names.append(os.path.splitext(faces)[0])

face_locations, face_encodings, face_names = [], [], []
scan_frame = True
present = set()

while True:
    __, frame = capture.read()
    frame = cv2.flip(frame, 1)
    min_frame = cv2.resize(frame, (0, 0), fx=0.2, fy=0.2)
    rgb_frame = cv2.cvtColor(min_frame, cv2.COLOR_BGR2RGB)

    if scan_frame:
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            same = face_recognition.compare_faces(train_face_encodings, face_encoding)
            name = "Unknown"

            dist = face_recognition.face_distance(train_face_encodings, face_encoding)
            best_match = np.argmin(dist)
            if same[best_match]:
                name = train_face_names[best_match]
            face_names.append(name)

    scan_frame = not scan_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 5
        right *= 5
        bottom *= 5
        left *= 5

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 69, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 69, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)
        present.add(name)

    cv2.imshow('Presence Check', frame)

    esc = cv2.waitKey(10) & 0xff
    if esc == 27:
        break

capture.release()
cv2.destroyAllWindows()

if "Unknown" in present:
    present.remove("Unknown")

if len(present) > 0:
    print(str(len(present)) + " people were detected in the frame. They are: ")
    print(i for i in present)
else:
    print("No one was detected.")
