const io = window.io;
const React = window.React;
const ReactDOM = window.ReactDOM;

const socket = io.connect();
socket.on("message", (message) => {
  console.log("Message Received!: " + message);
});

function App() {
  const [message, setMessage] = React.useState("");
  const sendMessage = () => {
    const messageObject = {
      timestamp: Date.now(),
      message: message,
    };
    socket.send("json", JSON.stringify(messageObject));
    console.log("Message sent: " + JSON.stringify(messageObject));
    setMessage("");
  };

  return (
    <>
      <textarea
        className="form-control flex-grow mx-2"
        id="message"
        value={message}
        onChange={(e) => {
          setMessage(e.target.value);
        }}
      ></textarea>
      <button className="btn btn-primary mx-2" onClick={sendMessage}>
        Send
      </button>
    </>
  );
}

const appNode = document.querySelector("#App");
const root = ReactDOM.createRoot(appNode);
root.render(<App />);
