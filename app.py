from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""

    if request.method == "POST":
        text = request.form.get("text")

        if text:
            translated_text = "Translated: " + text

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)