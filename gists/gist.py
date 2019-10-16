#!/usr/bin/python
"""
Update one file:
python gist.py <filename>

Update files in a folder:
python gist.py <folder>
"""
import os, requests, sys, json
import ipdb

username='peter.jp.xie@gmail.com'    #sys.argv[2]
password='peter_0909'                #sys.argv[3]

exts = ['.py']

files = []
if os.path.isfile(sys.argv[1]):
    files = [sys.argv[1]]
elif os.path.isdir(sys.argv[1]):
    for f in os.listdir(sys.argv[1]):
        for ext in exts:
            if f.endswith(ext):
                files.append(f)
                break                

for f in files: 
    content=open(f, 'r').read()
    filename = os.path.basename(f)
    data = {"files":{filename:{"content":content}},
            "description": filename,
            "public": True,
           }
    r = requests.post('https://api.github.com/gists',json.dumps(data),auth=requests.auth.HTTPBasicAuth(username, password)) 
    print(filename)
    print(r.status_code)
    print(r.json()['html_url'])
    print('\n')