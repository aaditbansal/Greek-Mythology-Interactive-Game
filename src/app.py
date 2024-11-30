from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string
import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
conversation_history = ""

app = Flask(__name__)
CORS(app)

def scrape_content(filename, title):
    with open(filename, 'r') as file:
        content = file.read()
    sections = content.split("\n\n")
    descriptions = {}
    for section in sections:
        if "~" in section:
            label, description = section.split("{", 1)
            descriptions[label.strip()] = description.strip()
    return descriptions.get(title, "Pretend to be a greek mythology character")


@app.route('/start-chat', methods=['GET'])
def start_chat():
    myth_name = request.args.get('myth')
    global conversation_history
    conversation_history = scrape_content("descriptions.txt", myth_name)
    if myth_name:
        # Generate a random letter from the alphabet
        print(myth_name)
        # random_letter = random.choice(string.ascii_letters)

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
    
# This route will process the user's input and generate a random letter
@app.route('/process-request', methods=['POST'])
def process_request():
    # Get the user input from the request
    data = request.get_json()
    user_input = data.get('userInput', '')
    global conversation_history

    conversation_history += "Provided above is the latest context on the conversation, and here is the next prompt ANSWER ONLY THIS CURRENT PROMPT:\n" + user_input + "\nremember, you are the aforementioned greek character!!\n"

    if user_input:
        # Generate a random letter from the alphabet
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
        
        # Return the random letter as a JSON response
        return jsonify({'randomLetter': summary})
    else:
        return jsonify({'error': 'No input provided'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
