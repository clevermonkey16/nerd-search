import React from "react";
function JobOverview({
  title,
  company,
  location,
  pay,
  datePosted,
  onClick,
  jobId,
  selected,
}) {
  const handleClick = () => {
    onClick(jobId);
  };
  return (
    <div
      className={`jobOverview ${selected ? "selectedJob" : ""}`}
      onClick={handleClick}>
      <div>{title}</div>
      <div>{company}</div>
      <div>{location}</div>
      <div>{pay}</div>
      <div>{datePosted}</div>
      <div>{selected}</div>
    </div>
  );
}

export default JobOverview;
