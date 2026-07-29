from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app) # Para que tu web de Github pueda hablar conmigo

# Tu API key segura, no va en el código público
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message")
    
    prompt = f"Eres Byte, un robot tierno y amable. Hablas con ^w^ y emojis. Responde corto en español a: {user_msg}"
    response = model.generate_content(prompt)
    
    return jsonify({"reply": f"Byte: {response.text}"})

if __name__ == "__main__":
    app.run()
