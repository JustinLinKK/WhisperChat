# .venv\Scripts\activate.bat

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder="../frontend")
app.config["TEMPLATES_AUTO_RELOAD"] = True
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def test_connect():
    print("CONNECTION RECEIVED")


@socketio.on("senderMessage")
def test_connect(message):
    print(f"Message received on senderMessage: {message}")


if __name__ == "__main__":
    socketio.run(app)
