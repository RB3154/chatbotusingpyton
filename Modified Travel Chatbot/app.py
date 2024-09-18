import google.generativeai as ai
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = 'AIzaSyD3j5vE2Udxpv_R6ZerkK4ATjvomkUIhQo'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

@app.route("/", methods=["GET", "POST"])
def index():
    bot_response = ""
    if request.method == "POST":
        user_message = request.form["message"]
        
        if user_message.lower() == 'bye':
            bot_response = "Goodbye!"
        else:
            response = chat.send_message(user_message)
            bot_response = response.text.strip()
    
    return render_template("index.html", bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
