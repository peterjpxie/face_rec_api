from flask import Flask, request
import os
import json
from face_util import compare_faces, face_rec

app = Flask(__name__)

@app.route('/face_match')
def face_match():
    if request.method == 'POST':
        # check if the post request has the file part
        if ('file1' in request.files) and ('file2' in request.files):        
            file1 = request.files.get('file1')
            file2 = request.files.get('file2')                         
            ret = compare_faces(file1, file2)     
            resp_data = {"match": bool(ret)} # convert numpy._bool to bool for json.dumps
            return json.dumps(resp_data)
                                          
@app.route('/face_rec')
def face_recognition():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' in request.files:
            file = request.files.get('file')                          
            name = face_rec(file)    
            resp_data = {'name': name }
            return json.dumps(resp_data)           
    
# When debug = True, code is reloaded on the fly while saved
app.run(host='0.0.0.0', port='5001', debug=True)