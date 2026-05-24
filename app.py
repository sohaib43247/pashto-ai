from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    translated_text = ""

    if request.method == "POST":

        user_text = request.form.get("text")

        if user_text:

            translated_text = GoogleTranslator(
                source='auto',
                target='ps'
            ).translate(user_text)

    return render_template(
        "index.html",
        translated_text=translated_text
    )

if __name__ == "__main__":
    app.run(debug=True)