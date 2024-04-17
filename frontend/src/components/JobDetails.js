import React from "react";

function JobDetails({
  title,
  company,
  location,
  pay,
  datePosted,
  jobId,
  link,
  description,
}) {
  return (
    <div className="jobDetails verticalContainer">
      <div>{title}</div>
      <div>{company}</div>
      <div>{location}</div>
      <div>{pay}</div>
      <div>{datePosted}</div>
      <div>{description}</div>
      <div>{jobId}</div>
      <a
        href={link}
        target="_blank"
        rel="noreferrer"
        className="applyButton">
        Apply
      </a>
    </div>
  );
}

export default JobDetails;
