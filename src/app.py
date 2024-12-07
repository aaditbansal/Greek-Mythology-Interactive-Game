from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string
import os
from dotenv import load_dotenv
import openai
import base64

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
conversation_history = ""

app = Flask(__name__)
CORS(app)

def scrape_content(filename, title):
    with open(filename, 'rb') as file:
        content = file.read()
    if True:
        content = base64.b64decode(content).decode()
    sections = content.split("}")
    descriptions = {}
    for section in sections:
        if "{" in section:
            label, description = section.split("{", 1)
            descriptions[label.strip()] = description.strip()
    return descriptions.get(title, "Pretend to be a greek mythology character")


@app.route('/start-chat', methods=['GET'])
def start_chat():
    myth_name = request.args.get('myth')
    global conversation_history
    conversation_history = scrape_content("descriptions.txt.b64", myth_name)
    if myth_name:
        print(myth_name) # making sure the right myth is selected
        response = openai.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": conversation_history
                }
            ],
            max_tokens=500,
            temperature=0.9,
            model="gpt-4o-mini",
        )
        summary = response.choices[0].message.content
        return jsonify({'randomLetter': summary})
    else:
        return jsonify({'error': 'No myth parameter provided'}), 400
    
@app.route('/process-request', methods=['POST'])
def process_request():
    # accepts the request from the user and stores it in data
    data = request.get_json()
    user_input = data.get('userInput', '')
    global conversation_history

    conversation_history += "Provided above is the latest context on the conversation, and here is the next prompt ANSWER ONLY THIS CURRENT PROMPT:\n" + user_input + "\nremember, you are the aforementioned greek character!!\n"

    if user_input:
        response = openai.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": conversation_history
                }
            ],
            max_tokens=500,
            temperature=0.7,
            model="gpt-4o-mini",
        )
        summary = response.choices[0].message.content
        conversation_history += "Your response to the above prompt:\n" + summary + "\n"
        
        # returns response to display on site
        return jsonify({'randomLetter': summary})
    else:
        return jsonify({'error': 'No input provided'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
