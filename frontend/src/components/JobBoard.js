import React from "react";
import JobOverviewPanel from "./JobOverviewPanel";
import JobDetails from "./JobDetails";
import { useState } from "react";

function JobBoard() {
  const [selectedJob, setSelectedJob] = useState(null);

  const handleClick = (jobId) => {
    setSelectedJob(jobId);
  };

  return (
    <div className="horizontalContainer">
      <JobOverviewPanel handleClick={handleClick} />
      <JobDetails
        title="Intern"
        company="Google"
        location="Mexico"
        pay="15"
        datePosted="June"
        jobId={selectedJob}
        link="https://www.google.com"
      />
    </div>
  );
}

export default JobBoard;
