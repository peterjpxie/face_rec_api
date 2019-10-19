@app.route('/face_rec', methods=['POST'])
def face_recognition():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' in request.files:
            file = request.files.get('file')                          
            name = face_rec(file)    
            resp_data = {'name': name }
            return json.dumps(resp_data)