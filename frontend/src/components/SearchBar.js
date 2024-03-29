import React from "react";

function SearchBar({ onChange }) {
  return (
    <div className="searchBarPanel">
      <input
        type="text"
        placeholder="Search..."
        onChange={onChange} // Call the onChange function passed as a prop
        className="searchBar"
      />
    </div>
  );
}

export default SearchBar;
