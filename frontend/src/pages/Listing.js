import React from "react";

import JobBoard from "../components/JobBoard";
import SearchBar from "../components/SearchBar";
import { useState, useEffect } from "react";

function Listing() {
  const [jobs, setJobs] = useState([]);
  const [companySearch, setCompanySearch] = useState("");

  const handleCompanyChange = (text) => {
    setCompanySearch(text);
    console.log(companySearch);
  };

  useEffect(() => {
    fetch("http://localhost:4000/jobs")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch jobs");
        }
        return response.json();
      })
      .then((data) => {
        setJobs(data);
      })
      .catch((error) => {
        console.error("Error fetching jobs:", error);
      });
  }, []);

  const filteredJobs = jobs.filter((job) =>
    job[0].toLowerCase().includes(companySearch.toLowerCase())
  );
  return (
    <div className="mainPage">
      <SearchBar onCompanyChange={handleCompanyChange} />
      <JobBoard jobs={filteredJobs} />
    </div>
  );
}

export default Listing;
