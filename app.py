from flask import Flask, render_template, request, jsonify
import os
import sys

# Add rag_chain directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "rag_chain")))

# Import chain
from llm_chain import conversational_chain

# Initialize Flask app and RAG chain
app = Flask(__name__)
_chain = conversational_chain()

# Global chat history
chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history
    user_input = request.json.get("message")

    # Append user message to chat history
    chat_history.append(f"User: {user_input}")

    try:
        result = _chain.invoke({"question": user_input})
        answer = result["answer"]
        chat_history.append(f"AI: {answer}")
    except Exception as e:
        answer = f"Error: {str(e)}"

    return jsonify({"response": answer})

@app.route("/reset", methods=["POST"])
def reset():
    global chat_history
    chat_history = []
    return jsonify({"status": "reset"})


if __name__ == "__main__":
    app.run(debug=True)
