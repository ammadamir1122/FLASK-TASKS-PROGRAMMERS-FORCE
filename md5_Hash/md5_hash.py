from flask import Flask, redirect, url_for,render_template
import hashlib

app = Flask(__name__)
@app.route('/')

def md5_hash():  
    im_path = "/home/ammadamir/myproject/image.png"
    with open(im_path, "rb") as f:
        im_bytes = f.read()
        im_hash = str(hashlib.md5(im_bytes).hexdigest())
    return 'Hash of your image is: ' + im_hash
