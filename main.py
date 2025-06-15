import os
from flask import Flask, request
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "✅ Chatbot API is live!"

@app.route("/backend", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"response": response.choices[0].message["content"]}
