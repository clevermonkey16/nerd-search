import React from "react";
import { useState } from "react";
import { useEffect } from "react";
import Tag from "./Tag";

function SearchBar({ onCompanyChange, onLocationChange, addTag, removeTag }) {
  const handleCompanyChange = (event) => {
    // Get the new text from the input field
    const newText = event.target.value;
    // Call the onCompanyChange function passed as a prop with the new text
    onCompanyChange(newText);
  };

  const handleLocationChange = (event) => {
    const newText = event.target.value;
    onLocationChange(newText);
  };

  const [tagSearchValue, setTagSearchValue] = useState("");
  const [suggestions, setSuggestions] = useState([
    "Backend Dev",
    "Data",
    "Databases",
    "Hardware",
    "IT/Devops",
    "Mobile Dev",
    "Networks",
    "Project Manager",
    "QA Tester",
    "Systems",
    "UI/UX Frontend",
  ]);
  const [showDropdown, setShowDropdown] = useState(false);
  const [availableTags, setAvailableTags] = useState([
    "Backend Dev",
    "Data",
    "Databases",
    "Hardware",
    "IT/Devops",
    "Mobile Dev",
    "Networks",
    "Project Manager",
    "QA Tester",
    "Systems",
    "UI/UX Frontend",
  ]);
  const [selectedTags, setSelectedTags] = useState([]);

  const tagsDict = {
    "Backend Dev": "backenddev",
    Data: "data",
    Databases: "databases",
    Hardware: "hardware",
    "IT/Devops": "itdevops",
    "Mobile Dev": "mobiledev",
    Networks: "networks",
    "Project Manager": "pm",
    "QA Tester": "qa",
    Systems: "systems",
    "UI/UX Frontend": "uiux",
  };

  const handleTagChange = (event) => {
    const inputText = event.target.value;
    setTagSearchValue(inputText);
    const suggestions = availableTags.filter((tag) =>
      tag.toLowerCase().includes(inputText.toLowerCase())
    );
    setSuggestions(suggestions);
    setShowDropdown(true);
  };

  const handleSuggestionClick = (tag) => {
    addTag(tagsDict[tag]);
    setSelectedTags((prevSelectedTags) => [...prevSelectedTags, tag]);
    setAvailableTags((prevTags) => prevTags.filter((t) => t !== tag));
    setTagSearchValue("");

    setShowDropdown(false);
  };

  useEffect(() => {
    const suggestions = availableTags.filter((tag) =>
      tag.toLowerCase().includes(tagSearchValue.toLowerCase())
    );
    setSuggestions(suggestions);
    const handleClickAnywhere = (event) => {
      const searchBarPanel = document.querySelector(".dropdown");
      // Check if the clicked element is inside the component
      if (searchBarPanel && searchBarPanel.contains(event.target)) {
        // Clicked inside the component, handle it here
        setShowDropdown(true);
        return;
      }
      setShowDropdown(false); // For example, close the dropdown
      // Clicked outside the component, handle it here
    };

    document.addEventListener("click", handleClickAnywhere); // Attach event listener to document
    return () => {
      document.removeEventListener("click", handleClickAnywhere); // Cleanup on component unmount
    };
  }, [showDropdown, availableTags, tagSearchValue]); // Add showDropdown to the dependencies to update the listener when it changes

  return (
    <div className="searchBarPanel">
      <div
        style={{
          marginRight: "1rem",
          width: "6rem !important",
          flexShrink: "0",
        }}>
        Search by:
      </div>
      <input
        style={{ width: "12rem" }}
        type="text"
        placeholder="Company name"
        onChange={handleCompanyChange} // Call the onChange function passed as a prop
        className="searchBar"
      />
      <input
        style={{ width: "12rem" }}
        type="text"
        placeholder="Location"
        onChange={handleLocationChange} // Call the onChange function passed as a prop
        className="searchBar"
      />

      <div className="dropdown">
        <input
          style={{ width: "12rem" }}
          type="text"
          placeholder="Job Tags"
          onChange={handleTagChange} // Call the onChange function passed as a prop
          value={tagSearchValue}
          className="searchBar"
        />
        {showDropdown && suggestions.length > 0 && (
          <div className="dropdown-menu show">
            {suggestions.map((tag, index) => (
              <button
                key={index}
                className="dropdown-item"
                type="button"
                onClick={() => handleSuggestionClick(tag)}>
                {tag}
              </button>
            ))}
          </div>
        )}
      </div>
      <div>
        {selectedTags.map((tag, index) => (
          <Tag
            key={index}
            tag={tag}
            onRemove={(removedTag) => {
              setSelectedTags(selectedTags.filter((t) => t !== removedTag));
              removeTag(tagsDict[removedTag]);
              setAvailableTags((prevTags) => [...prevTags, removedTag]);
            }}
          />
        ))}
      </div>
    </div>
  );
}

export default SearchBar;
