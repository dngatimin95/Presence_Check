# Presence Check
A simple alternative to checking attendance by detecting people through the computer's camera and recognizing them if their images are stored in the dataset. 

## What does this repo do?
This repo utilizes the face-recognition library and is a modified version of an example provided by ageitgey. Upon running the program, we first train a model with the faces that are stored within the charImages dataset. The face encodings and names are stored within the model and it is then ready to proceed. It then detects people's faces through the user's webcam based on the dataset that it has been provided with and remembers who has appeared on screen. After the webcam terminates, the various people that the model has detected will be printed out to show who appeared on screen.

## How do I run it?
