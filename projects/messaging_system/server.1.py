from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

app.run() # run(host="10.10.3.225", port=3000)