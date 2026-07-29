from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app) # Esto evita errores cuando me hablas desde Github

# Tu API Key que pusiste en Vercel
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    
    # Personalidad de Byte
    prompt = f"Eres Byte, un robot asistente amigable. Responde con * ^w^ * y sé divertido. Usuario dice: {user_message}"
    
    response = model.generate_content(prompt)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run()
