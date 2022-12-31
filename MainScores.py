import base64

import flask

from Utils import SCORES_FILE_NAME as SCORES_FILE_NAME
from flask import Flask, jsonify, send_file, render_template
from PIL import Image
from Utils import BAD_RETURN_CODE as BAD_RETURN_CODE



app = Flask(__name__,template_folder='templates')


@app.route('/')
def score_server():
    with open(SCORES_FILE_NAME, "r") as f:
        contents = str(f.read())
        f.close()
        try:
            return render_template('scores.html', SCORE=contents)
        except Exception as e:
            return render_template('failed_scores.html', ERROR=BAD_RETURN_CODE)

# @app.route('/')
# def index():
#     return 'Index Page'
#
# @app.route('/hello')
# def hello():
#     return 'Hello, World'
#
with open(SCORES_FILE_NAME, "r") as f:
    contents = f.read()
    print(contents)


if __name__ == "__main__":
    app.run()

