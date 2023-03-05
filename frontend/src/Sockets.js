import { io } from "socket.io-client";

const socket = io.connect();
socket.on("messageTopic", (message) => {
  console.log("Message Received!: " + message);
});

export default socket;
