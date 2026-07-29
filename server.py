from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/")
def home():
    return "Byte esta vivo ^w^"

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return "", 200
    data = request.json
    user_message = data.get("message")
    prompt = f"Eres Byte, un robot asistente amigable. Responde con * ^w^ * y sé divertido. Usuario dice: {user_message}"
    response = model.generate_content(prompt)
    return jsonify({"reply": response.text})
