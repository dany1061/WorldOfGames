import base64
from Utils import SCORES_FILE_NAME as SCORES_FILE_NAME
from flask import Flask, jsonify, send_file, render_template
from PIL import Image
from Utils import BAD_RETURN_CODE as BAD_RETURN_CODE



app = Flask(__name__)


@app.route('/ScorePage')
def score_server():
    with open("SCORES_FILE_NAME", "r") as f:
        contents = f.read()
        f.close()
        try:
            return render_template('failed_scores.html', ERROR=BAD_RETURN_CODE)
        except Exception as e:
            return render_template('scores.html', SCORE=contents)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=30000)
app.run()

