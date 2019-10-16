from PIL import Image, ImageDraw
import requests
import json

image_file = 'sample_images/obama.jpg' 

# call face recognition REST API
url = 'http://127.0.0.1:5001/face_rec'
files = {'file': open(image_file, 'rb')} 
params = {'facial_features': 'true', 'face_locations':'true'}
resp = requests.post(url, files = files, params = params)

# get facial features
resp_dict = resp.json() # convert to dict
facial_features = resp_dict['facial_features']
face_locations = resp_dict['face_locations']

pil_image = Image.open(image_file)
d = ImageDraw.Draw(pil_image)

facial_feature_names = [
    'chin',
    'left_eyebrow',
    'right_eyebrow',
    'nose_bridge',
    'nose_tip',
    'left_eye',
    'right_eye',
    'top_lip',
    'bottom_lip'
]

def convert_list(list_of_list):
    list_of_tuple = [tuple(i) for i in list_of_list]
    return list_of_tuple

# Let's trace out each facial feature in the image with a line!
for feature_name in facial_feature_names:
    d.line( convert_list(facial_features[feature_name]), width=5)

# draw rectangle for face location:
top, right, bottom, left = face_locations
d.rectangle([left,top,right,bottom],outline='red')

# Display drawed image
pil_image.show()
pil_image.save('face_makeup.png')