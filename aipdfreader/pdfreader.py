# Import necessary libraries
import fitz
import openai
from flask import Flask, request

# Create a Flask web application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'This is the home page'

# Define a route for uploading a PDF file via POST request
@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    global pdf_text

    # Check if a 'pdfFile' field is present in the request files
    if 'pdfFile' not in request.files:
        return 'No file part'

    pdf_file = request.files['pdfFile']

    # Check if a PDF file has been selected
    if pdf_file.filename == '':
        return 'No selected file'

    # Read the binary content of the uploaded PDF file
    pdf_contents = pdf_file.read()

    # Create a PDF document object from the binary content
    pdf_document = fitz.open(stream=pdf_contents, filetype="pdf")

    # Initialize an empty string to store the extracted text
    text = ""

    # Iterate through the pages and extract text
    for page in pdf_document:
        text += page.get_text()

    # Store the extracted text in a global variable
    pdf_text = text

    # Print the extracted text
    print(pdf_text)

    print('We got this far\n')

    # Check if PDF text is available for processing
    if pdf_text:
        print('In the if statement\n')
        # Set your OpenAI API key
        openai.api_key = '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'

        # Define a conversation in the format for chat completions
        conversation = [
            {"role": "user", "content": "build an .ics calendar file based on the assignments and exams in this file: " + pdf_text},
        ]

        print("Currently runniing... \n")

        # Make a request to the GPT-3.5-turbo model for completions
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            temperature=0.8,
            max_tokens=2000
        )
        print(response)
        print("were starting to write\n")

        # Write the response to the .ics file
        with open('calendar.ics', 'w') as file:
            file.write(response.choices[0].message['content'])

        print("Printed Successfully")
        return 'ICS file generated successfully'
    else:
        return 'PDF text not available, please upload a PDF file first'

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
