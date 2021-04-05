import base64
import requests

def test_face_rec_json():
    url = 'http://127.0.0.1:5001/face_rec'
    # encode image as base64 text string.
    # Note: Must convert output binary string from b64encode to an ascii string to form a JSON, e.g. b'abc' to 'abc'.
    with open('sample_images/obama2.jpg', 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('ascii')

    data = {'file_format':'jpg', 'image_data': image_data}
    params = {'facial_features': 'true', 'face_locations':'true'}
    resp = requests.post(url, json = data, params = params)
    print( 'face_rec response:\n', json.dumps(resp.json()) )