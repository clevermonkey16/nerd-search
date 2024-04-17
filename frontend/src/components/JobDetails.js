import React from "react";

function JobDetails({
  title,
  company,
  location,
  datePosted,
  jobId,
  link,
  description,
}) {
  return (
    <div className="jobDetails verticalContainer">
      <div className="detailsTitle">{title}</div>
      <div className="detailsCompany">{company}</div>
      <div>{location}</div>
      <div>{datePosted}</div>
      <a
        style={{ marginTop: "0.5rem", marginBottom: "0.5rem" }}
        href={link}
        target="_blank"
        rel="noreferrer"
        className="applyButton">
        Apply
      </a>
      <div>{description}</div>
    </div>
  );
}

export default JobDetails;
