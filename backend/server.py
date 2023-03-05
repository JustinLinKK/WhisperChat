# .venv\Scripts\activate.bat

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import json
import chatClientSender

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


# sendMessage handles a message that has to be sent from the frontend to another user
@socketio.on("messageTopic")
def sendMessage(message):
    decodedMessage = json.loads(message)
    # chatClientSender.send_message(message, decodedMessage["receiver"])
    responseMessage = {
        "sender": "[messageSender here]",
        "receiver": "localhost:3000",
        "message": f"I got your message at around {time.time()}",
    }
    print(f"Message received was: {message}")
    emit("messageTopic", json.dumps(responseMessage))


# forwardMessage allows a message to be sent from this client's backend
def forwardMessage(sender, receiver, message):
    output = {"sender": sender, "receiver": receiver, "message": message}
    emit("messageTopic", output)


if __name__ == "__main__":
    socketio.run(app, port=3000)
