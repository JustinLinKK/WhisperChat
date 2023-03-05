import { useState } from "react";
import MessageHistory from "./MessageHistory";
import socket from "../../Sockets";
import ChatBanner from "./ChatBanner";

export default function ChatInterface() {
  const [receiver, setReceiver] = useState("");
  const [message, setMessage] = useState("");
  const sendMessage = () => {
    const messageObject = {
      sender: "",
      receiver: receiver,
      message: message,
    };
    socket.emit("messageTopic", JSON.stringify(messageObject));
    console.log("Message sent: " + JSON.stringify(messageObject));
    setMessage("");
  };

  return (
    <>
      <div className="pt-4">
        <ChatBanner receiver={receiver} />
        <div className="d-flex">
          <label htmlFor="receiver" className="mx-2">
            Set Receiver:
          </label>
          <input
            id="receiver"
            className="flex-grow-1 mx-2"
            type="text"
            value={receiver}
            onChange={(e) => {
              setReceiver(e.target.value);
            }}
          />
        </div>

        <hr />
        <div className="ps-3">
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
      </div>
    </>
  );
}
