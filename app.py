from flask import Flask
from src.hello import mensaje

app = Flask(__name__)

@app.route("/")
def home():
    return mensaje()

if __name__ == "__main__":
    app.run(debug=False)