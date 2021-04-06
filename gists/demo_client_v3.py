import requests
import json
import base64

def test_face_match():
    url = 'http://127.0.0.1:5001/face_match'
    # open file in binary mode
    files = {'file1': open('sample_images/obama.jpg', 'rb'),
             'file2': open('sample_images/obama2.jpg', 'rb')}     
    resp = requests.post(url, files=files)
    print( 'face_match response:\n', json.dumps(resp.json()) )
    
def test_face_rec():
    url = 'http://127.0.0.1:5001/face_rec'
    # open file in binary mode
    files = {'file': open('sample_images/obama2.jpg', 'rb')} 
    params = {'facial_features': 'true', 'face_locations':'true'}
    resp = requests.post(url, files = files, params = params)
    print( 'face_rec response:\n', json.dumps(resp.json()) )

def test_face_rec_json():
    url = 'http://127.0.0.1:5001/face_rec'
    # encode image as base64 text string.
    # Note: Must convert output bytes string from b64encode to an ascii string to form a JSON, e.g. b'abc' to 'abc'.
    with open('sample_images/obama2.jpg', 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('ascii')

    data = {'file_format':'jpg', 'image_data': image_data}
    params = {'facial_features': 'true', 'face_locations':'true'}
    resp = requests.post(url, json = data, params = params)
    print( 'face_rec response:\n', json.dumps(resp.json()) )

def main():
    test_face_match()
    test_face_rec()
    test_face_rec_json()
    
if __name__ == '__main__':
    main()