from flask import Flask, render_template, request, jsonify
import chatbot_code  # Import your chatbot code

app = Flask(__name__)

@app.route('/')
def chatbot():
    return render_template('chatbot.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']

    # Process the user's input using the chatbot code
    bot_response = chatbot_code.process_question(user_input)

    return jsonify({'bot_response': bot_response})

if __name__ == "__main__":
    app.run()
