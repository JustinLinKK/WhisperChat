import ChatInterface from "./components/ChatInterface/ChatInterface";
import Chats from "./components/Chats";

function App() {
  return (
    <div className="overflow-visible">
      <div className="mb-5">
        <div className="row">
          <div className="col-3">
            <Chats />
          </div>
          <div className="col-9">
            <ChatInterface />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
