from flask import Flask
from flask import request
from flask import Response
from flask import send_file
import json
from PIL import ImageGrab


def server():

    app=Flask(__name__)

    @app.route('/')
    def init():
        return 'init'
    
    @app.route('/func',methods=['GET','POST'])
    def get():
        content = str(request.args.get('method'))
        if content=="screenshot":
            im=ImageGrab.grab()
            return Response(im)
        else:
            return "invaild method!"

    app.run(host='127.0.0.1',port=5000)

server()
