from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "hiunhfbhyho uihoho"

if __name__ == "__main__":
    app.run(port=1234, threaded =True)
