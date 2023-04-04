from flask import Flask, request

app = Flask(__name__)

@app.route('/square')
def square():
    number = request.args.get('number')
    if not number.isdigit():
        return 'Invalid number parameter'
                        
    number = int(number)
    result = number ** 2
    return 'The square of {} is {}'.format(number, result)


if __name__ == '__main__':
    app.run(debug=True)

