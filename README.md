# face_rec_api
Build a REST API for [face recognition](https://github.com/ageitgey/face_recognition) so you can use it to develop your own face recognition applications without the need to learn complicated machine learning. 

**API Endpoints:**
* face_recognition : return a matched person's ID, name, and optional feature details
* face_match : return if two images are matched for the same person.

# Notes
Many open source face recognition projects, like [face recognition](https://github.com/ageitgey/face_recognition), are for Linux / POSIX systems only. Building a REST API for them is a much easier solution than trying to convert and deploy them for mobile devices.
