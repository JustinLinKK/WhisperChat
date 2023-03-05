import Message from "./Message";

export default function MessageHistory({ messages }) {
  return (
    <>
      <div>
        {messages.map((message) => {
          return (
            <>
              {message.sender === "" ? (
                <Message content={message.message} alignRight />
              ) : (
                <Message content={message.message} />
              )}
            </>
          );
        })}
      </div>
    </>
  );
}
