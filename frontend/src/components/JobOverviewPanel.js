import React from "react";
import { useState } from "react";
import JobOverview from "./JobOverview";

function JobOverviewPanel({ handleClick }) {
  const [selectedJob, setSelectedJob] = useState(null);
  const handleClickAndSetJob = (jobId) => {
    handleClick(jobId);
    setSelectedJob(jobId);
  };
  return (
    <div className="verticalContainer jobOverviewPanel">
      <JobOverview
        title="Intern"
        company="Google"
        location="Mexico"
        pay="15"
        datePosted="June"
        onClick={handleClickAndSetJob}
        jobId="1"
        selected={selectedJob === "1" ? true : false}
      />
      <JobOverview
        title="Intern"
        company="Google"
        location="Mexico"
        pay="15"
        datePosted="June"
        jobId="2"
        onClick={handleClickAndSetJob}
        selected={selectedJob === "2" ? true : false}
      />
      <JobOverview
        title="Intern"
        company="Google"
        location="Mexico"
        pay="15"
        datePosted="June"
        jobId="3"
        onClick={handleClickAndSetJob}
        selected={selectedJob === "3" ? true : false}
      />
    </div>
  );
}

export default JobOverviewPanel;
