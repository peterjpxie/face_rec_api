@app.route('/face_rec', methods=['POST', 'GET'])
def face_recognition():
    if request.method == 'POST':
        # JSON data format
        if request.is_json:
            """ Sample data
            {'file_format':'jpg', 'image_data': <base64 ascii string>}
            """
            # print('Request is a JSON format.')
            json_data = request.get_json(cache=False)
            file_format = json_data.get('file_format', None)
            image_data = json_data.get('image_data', None)
            if file_format not in ALLOWED_EXTENSIONS or image_data is None:
                return '{"error":"Invalid JSON."}'

            file = os.path.join(UPLOAD_FOLDER, 'image.' + file_format)
            with open(file,'wb') as f:
                # Note: Convert ascii string to binary string first, e.g. 'abc' to b'abc', before decode as base64 string.
                f.write(base64.b64decode(image_data.encode('ascii'))) 
            
            name = face_rec(file)
            return json.dumps({'name': name })