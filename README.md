# Presence Check



## What does this repo do?
This repo utilizes the [face-recognition library](https://github.com/ageitgey/face_recognition) and is a modified version of an example provided by ageitgey. Upon running the program, the script will train a model first with the faces that are stored within the charImages dataset. These are the faces that the script will look out for, thus having a clear picture of the faces will be important. It works best when only the face is included and is facing forward with their facial features clearly observed. After the face encodings and names are stored within the model, it is ready to proceed. The script will then detect people's faces through the user's webcam based on the dataset that it has been provided with and records down who has appeared on screen. After the webcam terminates, the people that the model has detected will be printed out to show who has appeared on screen.

## How do I run it?
To run the script, download the entire repo and make sure you change the file path to where your charImages folder is before running it! You can add pictures of yourself or your friends onto the charImages folder so that the program can detect other people as well. Have fun!
