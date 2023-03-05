# .venv\Scripts\activate.bat

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import json

app = Flask(
    __name__,
    static_folder="../frontend/build/static",
    template_folder="../frontend/build",
)
app.config["TEMPLATES_AUTO_RELOAD"] = True
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def test_connect():
    print("CONNECTION RECEIVED")


@socketio.on("messageTopic")
def sendMessage(message):
    responseMessage = {
        "time": round(time.time()),
        "message": f"I got your message at around {time.time()}",
    }
    print(f"Message received was: {message}")
    emit("messageTopic", json.dumps(responseMessage))


def forwardMessage(message):
    emit("messageTopic", message)


if __name__ == "__main__":
    socketio.run(app, port=3000)
