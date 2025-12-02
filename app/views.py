import base64
import json
import os

from flask import render_template, request
from werkzeug.utils import secure_filename

from app import app
from app.ai import Ai


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cv = request.files['cv']
        # UGLYYYY, UPLOAD STRAIGHT BASE64 JEEEZZZ
        filename = secure_filename(cv.filename)
        cv.save(filename)  # todo: upload only pdf and in base64 through js? mb idk yet
        with open(filename, "rb") as file:
            file_data = file.read()
            encoded_cv = base64.b64encode(file_data).decode('utf-8')
        ai = Ai()
        cv_data = ai.parse_cv(encoded_cv)
        print(json.dumps(cv_data)) #request.data request.files[0]
        return json.dumps(cv_data)
    return render_template('index.html')

