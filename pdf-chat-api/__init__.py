from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
import os
from .langchain.methods import create_docsearch, query_docsearch

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/files'

os.environ["OPENAI_API_KEY"] = "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"

@app.route('/')
def hello_world():
    return 'Hello World!'

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
        print(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],filename))
        return 'File saved successfully'
    else:
        return 'Unsupported file type'

@app.route('/query', methods=['POST'])
def query_file():
    data = request.get_json()
    if 'query' and 'filename' not in data:
        return 'No query or file part'  
    query = data['query']
    filename = data['filename']
    file_path=  os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],filename)
    docsearch = create_docsearch(file_path)
    output = query_docsearch(docsearch,query)
    return output



