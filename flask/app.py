#from werkzeug.datastructures import TypeConversionDict 
import s3
from flask import Flask, render_template, redirect, request, jsonify
import s3
import os
from decouple import config
import requests


#key_env  =config('SECRET_ACCESS_KEY')
#id_env  =config('ACCESS_KEY_ID')
#print(id_env,key_env)
app = Flask(__name__)
#@app.route('/')
#def download():
#    s3.Download_file('hello.txt')
#    return redirect('/print')
@app.route('/print')
def print():
    s3.Download_file('hello.txt')
    with open('hello.txt', "r") as f:
      content = f.read()
    return (content)

@app.route('/log')
def log():
    text=request.args.get('text')
    body= {'log':text}
    requests.put('http://es01:9200/yarin')
    requests.post('http://es01:9200/yarin/as/engines', data={"name": "engine1"})
    requests.post('http://es01:9200/yarin/as/engines/engine1/logs/api',data=body)
    return ('the log that sent to elasticsearch is :  '+text)

app.run(host='0.0.0.0', port=5001, debug=True)
