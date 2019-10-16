import requests
import json

def test_face_match():
    url = 'http://127.0.0.1:5001/face_match'
    # open file in binary mode
    files = {'file1': open('sample_images/peter.jpg', 'rb'),
             'file2': open('sample_images/peter2.jpg', 'rb')}     
    resp = requests.post(url, files=files)
    print( 'face_match response:\n', json.dumps(resp.json()) )
    
if __name__ == '__main__':
    test_face_match()