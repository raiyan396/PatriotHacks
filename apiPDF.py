from flask import Flask, request
import fitz


app = Flask(__name__)


@app.route('/')
def home():
    return 'This is the home page'


@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'pdfFile' not in request.files:
        return 'No file part'

    pdf_file = request.files['pdfFile']

    if pdf_file.filename == '':
        return 'No selected file'

    # Handle the uploaded PDF file here (e.g., save it to a folder)
    # Example: pdf_file.save('uploads/' + pdf_file.filename)

    return 'File uploaded successfully'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
