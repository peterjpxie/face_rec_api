import face_recognition as fr

def compare_faces(file1, file2):
    """
    Compare two images and return True / False for matching.
    """
    # Load the jpg files into numpy arrays
    image1 = fr.load_image_file(file1)
    image2 = fr.load_image_file(file2)
    
    # Get the face encodings for each face in each image file
    # Assume there is only 1 face in each image, so get 1st face of an image.
    image1_encoding = fr.face_encodings(image1)[0]
    image2_encoding = fr.face_encodings(image2)[0]
    
    # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
    results = fr.compare_faces([image1_encoding], image2_encoding)    
    return results[0]

# Each face is tuple of (Name,sample image)    
known_faces = [('Peter','sample_images/peter.jpg'),
               ('Obama','sample_images/obama.jpg'),
              ]
    
def face_rec(file):
    """
    Return name for a known face, otherwise return 'Uknown'.
    """
    for name, known_file in known_faces:
        if compare_faces(known_file,file):
            return name
    return 'Unknown' 