import React from "react";
import JobOverviewPanel from "./JobOverviewPanel";
import JobDetails from "./JobDetails";
import { useState } from "react";

function JobBoard({ jobs }) {
  const [selectedJob, setSelectedJob] = useState([]);

  const handleClick = (title, company, location, datePosted, jobId) => {
    setSelectedJob([title, company, location, datePosted, jobId]);
  };

  return (
    <div className="horizontalContainer">
      <JobOverviewPanel
        handleClick={handleClick}
        jobs={jobs}
      />
      {selectedJob.length !== 0 && (
        <JobDetails
          title={selectedJob[0]}
          company={selectedJob[1]}
          location={selectedJob[2]}
          datePosted={selectedJob[3]}
          jobId={selectedJob[4]}
          link={selectedJob[4]}
        />
      )}
    </div>
  );
}

export default JobBoard;
