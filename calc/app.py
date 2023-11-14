from flask import Flask, request
import operations

app = Flask(__name__)

OPERATIONS = {
    'add': operations.add,
    'sub': operations.sub,
    'div': operations.div,
    'mult': operations.mult
}

def get_args(args):
    """
    Return args as a number
    @param args: dict, response dict
    @return: float, float
    """

    if args.get('a') and args.get('b'):
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))

        return a, b


@app.route('/add')
def add():
    a, b = get_args(request.args)
    return str(operations.add(a, b))


@app.route('/sub')
def sub():
    a, b = get_args(request.args)
    return str(operations.sub(a, b))


@app.route('/mult')
def mult():
    a, b = get_args(request.args)
    return str(operations.mult(a, b))

@app.route('/div')
def div():
    a, b = get_args(request.args)
    return str(operations.div(a, b))


@app.route('/math/<operation>')
def do_math(operation):
    a, b = get_args(request.args)
    return str(OPERATIONS[operation](a, b))
