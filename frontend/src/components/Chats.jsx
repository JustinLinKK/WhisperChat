import Chat from "./Chat";

export default function Chats() {
  return (
    <>
      <div className="border px-4 py-3">
        <h1 className="display-3">Chats</h1>
        <hr />
        <Chat name="John Doe" />
        <Chat name="Bill James" />
        <Chat name="Bob Ross" />
      </div>
    </>
  );
}
