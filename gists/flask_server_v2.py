from flask import Flask, request
import re, json
from face_util import compare_faces, face_rec

app = Flask(__name__)

@app.route('/face_match', methods=['POST'])
def face_match():
    if request.method == 'POST':
        # check if the post request has the file part
        if ('file1' in request.files) and ('file2' in request.files):        
            file1 = request.files.get('file1')
            file2 = request.files.get('file2')                         
            ret = compare_faces(file1, file2)     
            resp_data = {"match": bool(ret)} # convert numpy._bool to bool for json.dumps
            return json.dumps(resp_data)
            
def print_request(request):
    # Print request url
    print(request.url)
    # print relative headers
    print('content-type: "%s"' % request.headers.get('content-type'))
    print('content-length: %s' % request.headers.get('content-length'))
    # print body content
    body_bytes = request.get_data()
    # replace image raw data with string '<image raw data>'
    body_sub = re.sub(b'(\r\n\r\n)(.*?)(\r\n--)',br'\1<image raw data>\3', body_bytes,flags=re.DOTALL)
    print(body_sub.decode('utf-8'))
    
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