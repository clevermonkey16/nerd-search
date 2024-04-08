import React from "react";

import JobBoard from "../components/JobBoard";
import SearchBar from "../components/SearchBar";

function Listing() {
  return (
    <>
      <SearchBar />
      <JobBoard />
    </>
  );
}

export default Listing;
