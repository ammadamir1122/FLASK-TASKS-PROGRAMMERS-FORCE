from flask import Flask

app = Flask(__name__)

@app.route('/greet/<string:user_name>')
def greet_user(user_name):
    return '<h1>Hello ' + user_name + '</h1>'
if __name__ == '__main__':
    app.run(debug=True)

