import json

from flask import Flask, render_template, request
from werkzeug.wrappers import Response

import convert_utils


app = Flask(__name__)


def _invalid_request(msg):
    return Response(
        json.dumps({'message': msg}),
        status=400
    )


def _successful_response(result):
    return Response(
        json.dumps({'result': result}),
        status=200
    )


@app.route('/')
def main_page_view():
    return render_template('index.html')


@app.route('/convert_number/', methods=['POST'])
def convert_number_view():
    try:
        data = json.loads(request.data)
    except ValueError:
        return _invalid_request('Wrong JSON')

    try:
        return _successful_response(
            convert_utils.choice_convert_function(data['number'])
        )
    except convert_utils.InvalidProvidedValue as e:
        return _invalid_request(e.message)

if __name__ == '__main__':
    app.run(debug=True)
