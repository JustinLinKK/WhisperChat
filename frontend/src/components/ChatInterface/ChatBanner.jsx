export default function ChatBanner({ receiver }) {
  return (
    <>
      <div className="alert alert-secondary me-3">
        <h1>{receiver}</h1>
      </div>
    </>
  );
}
