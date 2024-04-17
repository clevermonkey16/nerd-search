import React from "react";

function SearchBar({ onCompanyChange }) {
  const handleCompanyChange = (event) => {
    // Get the new text from the input field
    const newText = event.target.value;
    // Call the onCompanyChange function passed as a prop with the new text
    onCompanyChange(newText);
  };

  return (
    <div className="searchBarPanel">
      <div style={{ marginRight: "1rem" }}>Search by:</div>
      <input
        type="text"
        placeholder="Company name"
        onChange={handleCompanyChange} // Call the onChange function passed as a prop
        className="searchBar"
      />
      <input
        type="text"
        placeholder="Location"
        onChange={onCompanyChange} // Call the onChange function passed as a prop
        className="searchBar"
      />
    </div>
  );
}

export default SearchBar;
