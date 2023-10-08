import fitz
import openai
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'This is the home page'


@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    global pdf_text

    if 'pdfFile' not in request.files:
        return 'No file part'

    pdf_file = request.files['pdfFile']

    if pdf_file.filename == '':
        return 'No selected file'

    pdf_contents = pdf_file.read()

    # Create a PDF document object from the binary content
    pdf_document = fitz.open(stream=pdf_contents, filetype="pdf")

    # Initialize an empty string to store the extracted text
    text = ""

    # Iterate through the pages and extract text
    for page in pdf_document:
        text += page.get_text()

    pdf_text = text
    # Print the extracted text
    print(pdf_text)

    print('We got this far\n')
    # Now you can use pdf_text to generate the .ics file
    if pdf_text:
        print('In the if statement\n')
        # Set your OpenAI API key
        openai.api_key = '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'

        # Define the conversation in the format for chat completions
        conversation = [
            {"role": "user", "content": "build an .ics calendar file based on the assignments and exams in this file: " + pdf_text},
        ]

        print("Conversed\n")
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
        with open('read.ics', 'w') as file:
            file.write(response.choices[0].message['content'])

        print("Printed Successfully")
        return 'ICS file generated successfully'
    else:
        return 'PDF text not available, please upload a PDF file first'

    return 'PDF file uploaded successfully'


# @app.route('/generate-ics', methods=['POST'])
# def generate_ics():
#     global pdf_text
#     print('We got this far\n')
#     # Now you can use pdf_text to generate the .ics file
#     if pdf_text:
#         print('In the if statement\n')
#         # Set your OpenAI API key
#         openai.api_key = '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'

#         # Define the conversation in the format for chat completions
#         conversation = [
#             {"role": "user", "content": "build an .ics calendar file based on the assignments and exams in this file: " + pdf_text},
#         ]

#         # Make a request to the GPT-3.5-turbo model for completions
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=conversation,
#             temperature=0.8,
#             max_tokens=2000
#         )

#         # Write the response to the .ics file
#         with open('read.ics', 'w') as file:
#             file.write(response.choices[0].message['content'])

#         print("Printed Successfully")
#         return 'ICS file generated successfully'
#     else:
#         return 'PDF text not available, please upload a PDF file first'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
