import React from "react";

import JobBoard from "../components/JobBoard";
import SearchBar from "../components/SearchBar";
import { useState, useEffect } from "react";

function Listing() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    console.log("Fetching data...");
    fetch("http://localhost:4000/jobs")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch jobs");
        }
        return response.json();
      })
      .then((data) => {
        setJobs(data);
        console.log(data);
      })
      .catch((error) => {
        console.error("Error fetching jobs:", error);
      });
  }, []);
  return (
    <>
      <SearchBar />
      <JobBoard />
    </>
  );
}

export default Listing;
