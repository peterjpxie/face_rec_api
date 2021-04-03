# face_rec_api
Build a REST API for [face recognition](https://github.com/ageitgey/face_recognition) so you can use it to develop your own face recognition applications without the need to learn complicated machine learning. 

**API Endpoints:**
* face_match : return if two images are matched for the same person.
* face_rec : return a matched person's ID, name, and optional face details (face location and facial features)

# Installation
Install [face_recognition](https://github.com/ageitgey/face_recognition) together with [dlib](http://dlib.net/) first.
Then run: pip install -r requirements.txt

# How to Run
## Prerequisites
Prepare some known faces as a database for face_rec API in sample_images folder, and modify known_faces in face_util.py accordingly.
```
# Each face is tuple of (Name,sample image)    
known_faces = [('Obama','sample_images/obama.jpg'),
               ('Peter','sample_images/peter.jpg'),
              ]
```
## Run API Server
python flask_server.py

## Run API client - Web
Simply open a web browser and enter:
http://127.0.0.1:5001/face_rec
http://127.0.0.1:5001/face_match

and upload image files.

## Run API client - Python
python demo_client.py 

## Run API client Advanced (draw face features)
python find_facial_features_in_picture_w_api.py 

![Example](./Medium/face_makeup_m.png)

# Medium Post
Check out the [medium post](https://towardsdatascience.com/build-face-recognition-as-a-rest-api-4c893a16446e?source=friends_link&sk=5b89a9cbfc997aee59743c504c3bf068) for more details.

# Notes
Many open source face recognition projects, like [face recognition](https://github.com/ageitgey/face_recognition), are easy to install in or only for Linux / POSIX systems. Building a REST API for them is a much easier solution than trying to convert and deploy them for mobile devices.
