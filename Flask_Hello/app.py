from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("flask.html")

@app.route("/Flask")
def Ritabrata():
    return "Hello Ritabrata"

if __name__ ==  "__main__":
    app.run(debug=True)
