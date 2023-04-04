from flask import Flask, request
import hashlib

app = Flask(__name__)

@app.route('/md5', methods=['POST'])
def md5():
    file = request.files['/home/ammadamir/myproject/image.png']
    file_bytes = file.read()
    file_hash = hashlib.md5(file_bytes).hexdigest()
    return file_hash

if __name__ == '__main__':
    app.run(debug=True)

