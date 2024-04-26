import React from "react";
import { useState, useRef } from "react";
import JobOverview from "./JobOverview";

function JobOverviewPanel({
  handleClick,
  jobs,
  startIndex,
  endIndex,
  onNextClick,
  onPrevClick,
  currentPage,
}) {
  const [selectedJob, setSelectedJob] = useState(null);
  const componentRef = useRef(null);

  const handleClickAndSetJob = (
    title,
    company,
    location,
    datePosted,
    onClick,
    jobId,
    description,
    degree,
    skills,
    salary
  ) => {
    handleClick(
      title,
      company,
      location,
      datePosted,
      jobId,
      description,
      degree,
      skills,
      salary
    );
    setSelectedJob(jobId);
  };
  const handlePrevClick = () => {
    onPrevClick();
    if (componentRef.current) {
      componentRef.current.scrollTop = 0;
    }
  };
  const handleNextClick = () => {
    onNextClick();
    if (componentRef.current) {
      componentRef.current.scrollTop = 0;
    }
  };
  return (
    <div
      className="verticalContainer jobOverviewPanel"
      ref={componentRef}>
      {jobs.length === 0 ? (
        <div
          style={{
            textAlign: "center",
            fontSize: "1.3rem",
            marginTop: "2rem",
          }}>
          No jobs found.
        </div>
      ) : (
        jobs.slice(startIndex, endIndex).map((job) => (
          <JobOverview
            key={job[5]}
            title={job[1]}
            company={job[0]}
            location={job[2]}
            datePosted={job[4]}
            jobId={job[5]}
            selected={selectedJob === job[5] ? true : false}
            onClick={handleClickAndSetJob}
            description={job[3]}
            degree={job[8]}
            skills={job[9]}
            salary={job[10]}
          />
        ))
      )}

      {/* Page Controls */}
      <div className="horizontalContainer pageControls">
        <button
          className="pageButton"
          style={{ marginRight: "2rem", marginLeft: "2rem" }}
          onClick={handlePrevClick}
          disabled={currentPage === 1}>
          Previous Page
        </button>
        <div className="pageNumber">{currentPage}</div>
        <button
          className="pageButton"
          onClick={handleNextClick}
          style={{ marginLeft: "2rem", marginRight: "2rem" }}
          disabled={endIndex >= jobs.length}>
          Next Page
        </button>
      </div>
      {/* End page controls */}
    </div>
  );
}

export default JobOverviewPanel;
