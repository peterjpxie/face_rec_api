@app.route('/face_rec', methods=['POST', 'GET'])
def face_recognition():
    if request.method == 'POST':
        print_request(request)        
        # check if the post request has the file part
        if 'file' in request.files:
            file = request.files.get('file')                          
            name = face_rec(file)    
            resp_data = {'name': name }
            return json.dumps(resp_data)      

    return '''
    <!doctype html>
    <title>Face Recognition</title>
    <h1>Upload an image</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''            
    
app.run(host='0.0.0.0', port='5001', debug=True)