import { useState } from "react";
import MessageHistory from "./MessageHistory";
import socket from "../Sockets";

export default function ChatInterface() {
  const [message, setMessage] = useState("");
  const sendMessage = () => {
    const messageObject = {
      timestamp: Date.now(),
      message: message,
    };
    socket.emit("messageTopic", JSON.stringify(messageObject));
    console.log("Message sent: " + JSON.stringify(messageObject));
    setMessage("");
  };

  return (
    <>
      <div className="pt-4 ps-3">
        <MessageHistory />
        <div className="d-flex">
          <textarea
            className="form-control flex-grow mx-2"
            id="message"
            value={message}
            onChange={(e) => {
              setMessage(e.target.value);
            }}
          ></textarea>
          <button
            className="btn btn-primary theme-blue mx-2"
            onClick={sendMessage}
          >
            Send
          </button>
        </div>
      </div>
    </>
  );
}
