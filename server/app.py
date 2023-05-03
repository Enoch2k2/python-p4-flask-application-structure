#!/usr/bin/env python3
import ipdb
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.route('/<string:username>')
def show(username):
    return f'<h1>Hello {username}</h1>'


# @app.route('/<int:num_1>/<string:operator>/<int:num_2>')
# def do_math(num_1, operator, num_2):
#     if operator == "add":
#         return f'<h1>{num_1 + num_2}</h1>'
#     elif operator == "subtract":
#         return f'<h1>{num_1 - num_2}</h1>'
#     elif operator == "multiply":
#         return f'<h1>{num_1 * num_2}</h1>'
#     elif operator == "divide":
#         return f'<h1>{num_1 / num_2}</h1>'
#     else:
#         return '<h1>Invalid operation</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
