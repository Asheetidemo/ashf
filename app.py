
from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS  # Allows frontend requests

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Set up Gemini API Key
API_KEY = "AIzaSyCYmA_pDIlDIcr2aofUosfgGtL8uMO9q0U"
genai.configure(api_key=API_KEY)

# Define API route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Empty message"}), 400

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
