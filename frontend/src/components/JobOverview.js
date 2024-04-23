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
  console.log(location);
  return (
    <div
      className={`jobOverview ${selected ? "selectedJob" : ""}`}
      onClick={handleClick}>
      <div className="overviewTitle">{title}</div>
      <div>{company}</div>
      <div>
        {location.split("\n").map((line, index) => {
          return (
            <React.Fragment key={index}>
              {line}
              {line !== "" && <br />}
            </React.Fragment>
          );
        })}
      </div>
      <div>{datePosted === "30" ? "Posted 30+ days ago" : datePosted}</div>
      <div>{selected}</div>
    </div>
  );
}

export default JobOverview;
