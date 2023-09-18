from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    return f'{parameter}'

@app.route('/count/<parameter>')
def display_count(parameter):
    try:
        n = int(parameter)
        if n >= 0:
            # Generate a string with numbers from 0 to n-1, each separated by a newline character
            count = '\n'.join(str(i) for i in range(n))
            # Adding a trailing newline to match the test expectation
            return count + '\n'
    except ValueError:
        pass
    return 'Invalid parameter'


@app.route('/math/<int:a>/<op>/<int:b>')
def math_operation(a, op, b):
    if op == '+':
        return str(a + b)
    elif op == '-':
        return str(a - b)
    elif op == '*':
        return str(a * b)
    elif op == 'div':
        return str(float(a) / b)
    elif op == '%':
        return str(a % b)
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
