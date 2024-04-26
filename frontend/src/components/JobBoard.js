import React from "react";
import JobOverviewPanel from "./JobOverviewPanel";
import JobDetails from "./JobDetails";
import { useState } from "react";

function JobBoard({
  jobs,
  startIndex,
  endIndex,
  onNextClick,
  onPrevClick,
  currentPage,
}) {
  const [selectedJob, setSelectedJob] = useState([]);

  const handleClick = (
    title,
    company,
    location,
    datePosted,
    jobId,
    description,
    degree,
    skills,
    salary
  ) => {
    setSelectedJob([
      title,
      company,
      location,
      datePosted,
      jobId,
      description,
      degree,
      skills,
      salary,
    ]);
  };
  return (
    <div className="horizontalContainer jobBoard">
      <JobOverviewPanel
        handleClick={handleClick}
        jobs={jobs}
        startIndex={startIndex}
        endIndex={endIndex}
        onNextClick={onNextClick}
        onPrevClick={onPrevClick}
        currentPage={currentPage}
      />
      {selectedJob.length !== 0 && (
        <JobDetails
          title={selectedJob[0]}
          company={selectedJob[1]}
          location={selectedJob[2]}
          datePosted={selectedJob[3]}
          jobId={selectedJob[4]}
          link={selectedJob[4]}
          description={selectedJob[5]}
          degree={selectedJob[6]}
          skills={selectedJob[7]}
          salary={selectedJob[8]}
        />
      )}
    </div>
  );
}

export default JobBoard;
