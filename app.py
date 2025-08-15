from flask import Flask, request, jsonify, send_from_directory
from chatbot import get_chatbot_response
import os

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    if not user_input.strip():
        return jsonify({"error": "Message cannot be empty"}), 400

    bot_reply = get_chatbot_response(user_input)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
