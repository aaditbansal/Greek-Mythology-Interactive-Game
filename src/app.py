from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

@app.route('/start-chat', methods=['GET'])
def start_chat():
    myth_name = request.args.get('myth')
    if myth_name:
        # Generate a random letter from the alphabet
        print(myth_name)
        random_letter = random.choice(string.ascii_letters)
        return jsonify({'randomLetter': random_letter})
    else:
        return jsonify({'error': 'No myth parameter provided'}), 400
    
# This route will process the user's input and generate a random letter
@app.route('/process-request', methods=['POST'])
def process_request():
    # Get the user input from the request
    data = request.get_json()
    user_input = data.get('userInput', '')

    if user_input:
        # Generate a random letter from the alphabet
        random_letter = random.choice(string.ascii_letters)
        
        # Return the random letter as a JSON response
        return jsonify({'randomLetter': random_letter})
    else:
        return jsonify({'error': 'No input provided'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
