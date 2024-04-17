import React from "react";
function JobOverview({
  title,
  company,
  location,
  datePosted,
  onClick,
  jobId,
  selected,
  description,
}) {
  const handleClick = () => {
    onClick(title, company, location, datePosted, onClick, jobId, description);
  };
  return (
    <div
      className={`jobOverview ${selected ? "selectedJob" : ""}`}
      onClick={handleClick}>
      <div className="overviewTitle">{title}</div>
      <div>{company}</div>
      <div>{location}</div>
      <div>{datePosted.replace(/[^0-9\-/]/g, "")}</div>
      <div>{selected}</div>
    </div>
  );
}

export default JobOverview;
