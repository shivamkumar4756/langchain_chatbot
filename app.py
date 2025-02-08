from flask import Flask, request, jsonify
from dotenv import load_dotenv
from data_loader import load_and_preprocess_data
from vector_store import create_vector_store
from chatbot import initialize_chatbot

load_dotenv()

app = Flask(__name__)

docs = load_and_preprocess_data()
vector_db = create_vector_store(docs)
chatbot = initialize_chatbot()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("query")
    response = chatbot.run(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
