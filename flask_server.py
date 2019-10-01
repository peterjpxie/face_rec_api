"""
Install:
pip install flask

Run with python CLI:
python flask_server.py

"""

from flask import Flask, request, send_file, render_template, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
# import ipdb # import ipdb will disable the debug mode, i.e. reload on save file.
import pdb
import json
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

''' file uploads
http://flask.palletsprojects.com/en/1.0.x/patterns/fileuploads/
''' 
UPLOAD_FOLDER = 'image_files'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
                               
@app.route('/face_recognition', methods=['POST', 'GET'])
def face_recognition():
    if request.method == 'POST':
        # print(request.get_data().decode('utf-8'))
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files.get('file')
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if allowed_file(file.filename):
            # read file as image directly
            img = Image.open(file)
            newfilename = 'new.png'
            img.save(newfilename)
            
            ''' or convert string to numpy array
            #read image file string data
            filestr = request.files['file'].read()
            #convert string data to numpy array
            npimg = numpy.fromstring(filestr, numpy.uint8)
            # convert numpy array to image
            img = cv2.imdecode(npimg, cv2.CV_LOAD_IMAGE_UNCHANGED)
            '''            
                        
            # get parameters from url if any
            param_features = request.args.get('features', '')
            # read file content directly. 
            # Note once read or open by Image.open, the file becomes empty when try to save later. Cursor issue, IMO.
            # print('file content:\n', file.read()) 
            filename = secure_filename(file.filename) # secure_filename converts to a secure filename.
            # file.save(os.path.join(UPLOAD_FOLDER, filename))
            # return redirect(url_for('uploaded_file', filename=filename))
            # return send_from_directory(UPLOAD_FOLDER, filename)
            if param_features.lower() == 'true':
                pass # to add logic
            resp_data = {'ID':'', 'name': 'unknown',
                        'features': {}
                        }

            return json.dumps(resp_data)
            
    return '''
    <!doctype html>
    <title>Face Recognition</title>
    <h1>Upload a image</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/face_match', methods=['POST', 'GET'])
def face_match():
    if request.method == 'POST':
        # print(request.get_data().decode('utf-8'))
        # check if the post request has the file part
        if ('file1' not in request.files) or ('file2' not in request.files):
            flash('No file part')
            return redirect(request.url)
        
        file1 = request.files.get('file1')
        file2 = request.files.get('file2')
        # if user does not select file, browser also
        # submit an empty part without filename
        if file1.filename == '' or file2.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if allowed_file(file1.filename) and allowed_file(file2.filename):
            # read file as image directly
            img1 = Image.open(file1)
            img2 = Image.open(file2)
            new_filename1 = 'new1.png'
            new_filename2 = 'new2.png'
            img1.save(new_filename1)
            img2.save(new_filename2)
            
            ''' or convert string to numpy array
            #read image file string data
            filestr = request.files['file'].read()
            #convert string data to numpy array
            npimg = numpy.fromstring(filestr, numpy.uint8)
            # convert numpy array to image
            img = cv2.imdecode(npimg, cv2.CV_LOAD_IMAGE_UNCHANGED)
            '''            
                        
            # get parameters from url if any
            param_features = request.args.get('features', '')
            # read file content directly. 
            # Note once read or open by Image.open, the file becomes empty when try to save later. Cursor issue, IMO.
            # print('file content:\n', file.read()) 
            filename1 = secure_filename(file1.filename) # secure_filename converts to a secure filename.
            # file.save(os.path.join(UPLOAD_FOLDER, filename))
            # return redirect(url_for('uploaded_file', filename=filename))
            # return send_from_directory(UPLOAD_FOLDER, filename)
            if param_features.lower() == 'true':
                pass # to add logic
            resp_data = {'ID':'', 'name': 'unknown',
                        'features': {}
                        }

            return json.dumps(resp_data)
            
    return '''
    <!doctype html>
    <title>Face Match</title>
    <h1>Upload two images</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file1>
      <input type=file name=file2>
      <input type=submit value=Upload>
    </form>
    '''

# Request headers
# http://flask.pocoo.org/docs/1.0/api/#flask.Request
# https://werkzeug.palletsprojects.com/en/0.15.x/datastructures/#werkzeug.datastructures.Headers
@app.route('/request_headers')
def test_req_headers():
    headers = request.headers
    
    # Get header values
    # get(key, default=None, type=None, as_bytes=False)
    # Return None if not found
    user_agent = headers.get('User-Agent')
    if user_agent is not None:
        return 'Header User-Agent in the request is %s.' % user_agent 
    else:
        return 'Header User-Agent does not exist in the request.'

# Request body content
# http://flask.pocoo.org/docs/1.0/api/#flask.Request
@app.route('/request_body', methods=['POST', 'GET'])
def test_req_body():
    # get_data(cache=True, as_text=False, parse_form_data=False)
    request_body = request.get_data()
    request_body = request_body.decode('utf-8') # decode if it is byte string b''
    return 'Request body content is\n%s' % request_body
    
    # Output for request with '{"key1":"value1","key2":2}':
    # Request body content is b'{"key1":"value1","key2":2}'

# Request body content as JSON    
# Parse and return the data as JSON. If the mimetype does not indicate JSON (application/json, see is_json), this returns None unless force is true.     
@app.route('/request_body_json', methods=['POST', 'GET'])
def test_req_body_json():
    # get_json(force=False, silent=False, cache=True)
    # Note: return is actually a dict
    
    # Note: is_json is changed to a property than a method.
    if request.is_json:
        return 'Request body content as json:\n%s' % json.dumps(request.get_json(cache=False),indent=4)
    else:
        return r'Request has no header application/json.'

@app.route('/request_body_force_json', methods=['POST', 'GET'])
def test_req_body_force_json():
    return 'Request body content forced as json:\n%s' % json.dumps(request.get_json(force=True, cache=False),indent=4)
    '''Output example:
    Request body content forced as json:
    {
        "key1": "value1",
        "key2": 2
    }
    '''


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/sys_cmd')
def run_sys_cmd():
    return render_template('run_sys_cmd.html')
    
# return a file
# http://flask.pocoo.org/docs/1.0/api/#flask.send_file
@app.route('/download_file', methods=['POST', 'GET'])
@app.route('/download_file/<file>', methods=['POST', 'GET'])
def test_download_file(file='pytest.ini'):
    try:
        # return send_file('report.zip', as_attachment = True, attachment_filename='report.zip') # zip file
        return send_file(file, as_attachment = True, attachment_filename=file) # any file
    except Exception as e:
        return str(e)
    
# Run in HTTP  
# When debug = True, code is reloaded on the fly while saved
app.run(host='0.0.0.0', port='5001', debug=True)    

# Run in HTTPS
# https://werkzeug.palletsprojects.com/en/0.15.x/serving/#quickstart
ssl_context_ = ('ssl_keys/key.crt', 'ssl_keys/key.key')
# app.run(host='127.0.0.1', port='5000', ssl_context=ssl_context_)
# output: Running on https://127.0.0.1:5001/
