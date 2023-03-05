export default function Message({ alignRight }) {
  return (
    <>
      <div className="row">
        {alignRight && <div className="col-6"></div>}
        <div className="col-6">
          <div className="alert alert-info theme-blue">Hello</div>
        </div>
      </div>
    </>
  );
}
