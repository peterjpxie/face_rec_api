import requests
import os
# import ipdb # import ipdb will disable the debug mode, i.e. reload on save file.
import pdb
import json
# import matplotlib.pyplot as plt
# from PIL import Image
import numpy as np

# Pretty print whole request and response
# argument is request object
def pretty_print_request(request, decode=None, body_len=None):
    '''
    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    '''
    if decode:
        request_body = request.body.decode(decode)
    else:
        request_body = request.body
    
    if body_len and isinstance(body_len, int):
        request_body = request_body[:body_len]
        
    print('\n{}\n{}\n{}\n\n{}'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request_body # request.body[:500] # request.body.decode('utf-8')
        ))

# argument is response object         
def pretty_print_response(response):
    '''
    Pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    '''
    print('\n{}\n{}\n\n{}\n\n{}'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text # response.text[:500]
        ))        

# argument is request object
# display body in json format explicitly with expected indent. Actually most of the time it is not very necessary because body is formatted in pretty print way.    
def pretty_print_request_json(request):
    '''
    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    '''
    # ipdb.set_trace()
    print('\n{}\n{}\n{}\n\n{}'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        json.dumps(ast.literal_eval(request.body),indent=4))
        )
        
# argument is response object 
# display body in json format explicitly with expected indent. Actually most of the time it is not very necessary because body is formatted in pretty print way.    
def pretty_print_response_json(response):
    '''
    Pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    '''
    print('\n{}\n{}\n\n{}\n\n{}'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        json.dumps(response.json(),indent=4)
        ))

def test_face_rec():
    """
    
    """
    # url = 'https://httpbin.org/post' # It simply returns what it receives.
    url = 'http://127.0.0.1:5001/face_recognition'
    # open file in binary mode
    files = {'file': open('image_files/test.png', 'rb')}              # image file
    # files = {'file': ('newname.py',open('a.py', 'rb')) }  # change filename
    # files = {'file1': open('a.py', 'rb'),'file2': open('ClassOne.py', 'rb')} # two files
    params = {'key1': 'value1'}             # additional params
    r = requests.post(url, files = files, params = params)
    pretty_print_request(r.request, body_len=200)
    pretty_print_response(r)
    
def main():
    test_face_rec()
    
if __name__ == '__main__':
    main()