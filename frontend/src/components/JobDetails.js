import React from "react";
import { useRef, useEffect } from "react";

function JobDetails({
  title,
  company,
  location,
  datePosted,
  jobId,
  link,
  description,
  degree,
  skills,
  salary,
}) {
  const componentRef = useRef(null);
  const prevJobIdRef = useRef(jobId);
  useEffect(() => {
    // Check if the current value of myVariable is different from the previous value
    if (jobId !== prevJobIdRef.current) {
      // If it's different, execute the onChange function
      if (componentRef.current) {
        componentRef.current.scrollTop = 0;
      }

      // Update the previous value to the current value
      prevJobIdRef.current = prevJobIdRef;
    }
  }, [jobId]);
  return (
    <div
      className="jobDetails verticalContainer"
      ref={componentRef}>
      <div className="detailsTitle">{title}</div>
      <div className="detailsCompany">{company}</div>
      <div>
        Locations: <br />
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
      <a
        style={{ marginTop: "0.5rem", marginBottom: "0.5rem" }}
        href={link}
        target="_blank"
        rel="noreferrer"
        className="applyButton">
        Apply
      </a>
      <div>
        {description.split("\n").map((line, index) => {
          return (
            <React.Fragment key={index}>
              {line}
              {line !== "" && <br />}
            </React.Fragment>
          );
        })}
      </div>
      <div>{degree}</div>
      <div>{skills}</div>
      <div>{salary}</div>
    </div>
  );
}

export default JobDetails;
