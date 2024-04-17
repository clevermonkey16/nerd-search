import React from "react";
import { useState } from "react";
import JobOverview from "./JobOverview";

function JobOverviewPanel({ handleClick, jobs }) {
  const [selectedJob, setSelectedJob] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);

  const itemsPerPage = 10;
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;

  const handleClickAndSetJob = (
    title,
    company,
    location,
    datePosted,
    onClick,
    jobId,
    description
  ) => {
    handleClick(title, company, location, datePosted, jobId, description);
    setSelectedJob(jobId);
  };

  const nextPage = () => {
    setCurrentPage(currentPage + 1);
  };

  const prevPage = () => {
    setCurrentPage(currentPage - 1);
  };
  return (
    <div className="verticalContainer jobOverviewPanel">
      {jobs.slice(startIndex, endIndex).map((job) => {
        return (
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
          />
        );
      })}

      {/* Page Controls */}
      <div className="horizontalContainer pageControls">
        <button
          className="pageButton"
          style={{ marginRight: "2rem", marginLeft: "2rem" }}
          onClick={prevPage}
          disabled={currentPage === 1}>
          Previous Page
        </button>
        <div className="pageNumber">{currentPage}</div>
        <button
          className="pageButton"
          onClick={nextPage}
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
