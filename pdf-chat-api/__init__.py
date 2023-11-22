from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/files'

@app.route('/upload', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],filename))
        return 'File saved successfully'
    else:
        return 'Unsupported file type'



