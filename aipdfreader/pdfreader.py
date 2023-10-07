import fitz
import openai

doc = fitz.open('aipdfreader/schedule.pdf')

for page in doc:
    text = page.get_text()
    
# Set your OpenAI API key
openai.api_key = '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'

# Define the conversation in the format for chat completions
conversation = [
    {"role": "user", "content": "build an .ics calendar file based on the assignments and exams in this file: " + text},
]

# Make a request to the GPT-3.5-turbo model for completions
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation,
    temperature=0.8,
    max_tokens=2000
)

file = open('read.ics', 'w') 
file.write(response.choices[0].message['content']) 
print("Printed Successfully")
file.close()
# Print the response

