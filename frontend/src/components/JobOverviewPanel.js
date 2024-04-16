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
    jobId
  ) => {
    handleClick(title, company, location, datePosted, jobId);
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
            title={job[0]}
            company="A company"
            location={job[1]}
            datePosted={job[3]}
            jobId={job[4]}
            selected={selectedJob === job[4] ? true : false}
            onClick={handleClickAndSetJob}
          />
        );
      })}

      {/* Page Controls */}
      <div className="horizontalContainer pageControls">
        <button
          onClick={prevPage}
          disabled={currentPage === 1}>
          Previous Page
        </button>
        <button
          onClick={nextPage}
          disabled={endIndex >= jobs.length}>
          Next Page
        </button>
      </div>
      {/* End page controls */}
    </div>
  );
}

export default JobOverviewPanel;
