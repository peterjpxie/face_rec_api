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
    unknown_face_encoding = fr.face_encodings(unknown_image)[0]
    
    # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
    results = fr.compare_faces([image1_encoding], image2_encoding)
    
    return results[0]