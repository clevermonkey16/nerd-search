import React from "react";

import JobBoard from "../components/JobBoard";
import SearchBar from "../components/SearchBar";
import { useState, useEffect } from "react";

function Listing() {
  const [jobs, setJobs] = useState([]);
  const [companySearch, setCompanySearch] = useState("");
  const [locationSearch, setLocationSearch] = useState("");
  const [tags, setTags] = useState([]);

  const handleCompanyChange = (text) => {
    setCompanySearch(text);
  };
  const handleLocationChange = (text) => {
    setLocationSearch(text);
  };

  const addTag = (tag) => {
    setTags([...tags, tag]);
    // Include logic to apply the tag to your search criteria
  };
  const removeTag = (removedTag) => {
    setTags(tags.filter((tag) => tag !== removedTag));
  };

  useEffect(() => {
    const states = [
      ["Alabama", "AL"],
      ["Alaska", "AK"],
      ["American Samoa", "AS"],
      ["Arizona", "AZ"],
      ["Arkansas", "AR"],
      ["Armed Forces Americas", "AA"],
      ["Armed Forces Europe", "AE"],
      ["Armed Forces Pacific", "AP"],
      ["California", "CA"],
      ["Colorado", "CO"],
      ["Connecticut", "CT"],
      ["Delaware", "DE"],
      ["District Of Columbia", "DC"],
      ["Florida", "FL"],
      ["Georgia", "GA"],
      ["Guam", "GU"],
      ["Hawaii", "HI"],
      ["Idaho", "ID"],
      ["Illinois", "IL"],
      ["Indiana", "IN"],
      ["Iowa", "IA"],
      ["Kansas", "KS"],
      ["Kentucky", "KY"],
      ["Louisiana", "LA"],
      ["Maine", "ME"],
      ["Marshall Islands", "MH"],
      ["Maryland", "MD"],
      ["Massachusetts", "MA"],
      ["Michigan", "MI"],
      ["Minnesota", "MN"],
      ["Mississippi", "MS"],
      ["Missouri", "MO"],
      ["Montana", "MT"],
      ["Nebraska", "NE"],
      ["Nevada", "NV"],
      ["New Hampshire", "NH"],
      ["New Jersey", "NJ"],
      ["New Mexico", "NM"],
      ["New York", "NY"],
      ["North Carolina", "NC"],
      ["North Dakota", "ND"],
      ["Northern Mariana Islands", "NP"],
      ["Ohio", "OH"],
      ["Oklahoma", "OK"],
      ["Oregon", "OR"],
      ["Pennsylvania", "PA"],
      ["Puerto Rico", "PR"],
      ["Rhode Island", "RI"],
      ["South Carolina", "SC"],
      ["South Dakota", "SD"],
      ["Tennessee", "TN"],
      ["Texas", "TX"],
      ["US Virgin Islands", "VI"],
      ["Utah", "UT"],
      ["Vermont", "VT"],
      ["Virginia", "VA"],
      ["Washington", "WA"],
      ["West Virginia", "WV"],
      ["Wisconsin", "WI"],
      ["Wyoming", "WY"],
    ];
    const processJobs = () => {
      setJobs((jobs) => {
        return jobs.map((job) => {
          return job.map((item, itemIndex) => {
            if (itemIndex === 4) {
              return item.replace(/[^0-9\-/]/g, "");
            } else if (itemIndex === 2) {
              let tmpString = item;
              tmpString = tmpString.replace(
                /\bUnited States(?: of America)?\b/g,
                "US"
              );
              for (let i = 0; i < states.length; i++) {
                const [fullName, abbreviation] = states[i];
                if (tmpString.includes(fullName)) {
                  tmpString = tmpString.replace(
                    new RegExp(fullName, "g"),
                    abbreviation
                  );
                }
              }
              let locations = tmpString.split("\n");
              let res = "";
              for (let i = 0; i < locations.length; i++) {
                if (locations[i][0] === "") {
                  continue;
                }
                let tokens = locations[i].split(", ");
                let val1 = tokens[0];
                let val2 = tokens[1];
                let val3 = tokens[2];
                let city;
                let state;
                let country;
                if (val1 === "US" || val1 === "UK") {
                  country = val1;
                } else if (val2 === "US" || val2 === "UK") {
                  country = val2;
                } else if (val3 === "US" || val3 === "UK") {
                  country = val3;
                }
                if (val1.length === 2 && val1 !== "US" && val1 !== "UK") {
                  state = val1;
                } else if (
                  val2 &&
                  val2.length === 2 &&
                  val2 !== "US" &&
                  val2 !== "UK"
                ) {
                  state = val2;
                } else if (
                  val3 &&
                  val3.length === 2 &&
                  val3 !== "US" &&
                  val3 !== "UK"
                ) {
                  state = val3;
                }
                if (val1.length > 2) {
                  city = val1;
                } else if (val2 && val2.length > 2) {
                  city = val2;
                } else if (val3 && val3.length > 2) {
                  city = val3;
                }
                let tmp = "";
                if (city !== undefined) {
                  tmp += city
                    .toLowerCase()
                    .replace(/\b(us)\b|\b\w/g, (match, group) =>
                      group ? group.toUpperCase() : match.toUpperCase()
                    );
                }
                if (state !== undefined) {
                  if (city !== undefined) {
                    tmp += ", " + state;
                  } else {
                    tmp += state;
                  }
                }
                if (country !== undefined) {
                  if (tmp.length > 0) {
                    tmp += ", " + country;
                  } else {
                    tmp += country;
                  }
                }
                res += tmp;
                res += "\n";
              }

              return res;
            }
            return item;
          });
        });
      });
    };
    const url = "http://localhost:4000";
    //const url = "https://psych-website.onrender.com";
    fetch(url + "/jobs")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch jobs");
        }
        return response.json();
      })
      .then((data) => {
        setJobs(data);
      })
      .then(() => {
        processJobs();
      })
      .catch((error) => {
        console.error("Error fetching jobs:", error);
      });
  }, []);
  const stateAbbreviations = {
    AL: "Alabama",
    AK: "Alaska",
    AZ: "Arizona",
    AR: "Arkansas",
    CA: "California",
    CO: "Colorado",
    CT: "Connecticut",
    DE: "Delaware",
    FL: "Florida",
    GA: "Georgia",
    HI: "Hawaii",
    ID: "Idaho",
    IL: "Illinois",
    IN: "Indiana",
    IA: "Iowa",
    KS: "Kansas",
    KY: "Kentucky",
    LA: "Louisiana",
    ME: "Maine",
    MD: "Maryland",
    MA: "Massachusetts",
    MI: "Michigan",
    MN: "Minnesota",
    MS: "Mississippi",
    MO: "Missouri",
    MT: "Montana",
    NE: "Nebraska",
    NV: "Nevada",
    NH: "New Hampshire",
    NJ: "New Jersey",
    NM: "New Mexico",
    NY: "New York",
    NC: "North Carolina",
    ND: "North Dakota",
    OH: "Ohio",
    OK: "Oklahoma",
    OR: "Oregon",
    PA: "Pennsylvania",
    RI: "Rhode Island",
    SC: "South Carolina",
    SD: "South Dakota",
    TN: "Tennessee",
    TX: "Texas",
    UT: "Utah",
    VT: "Vermont",
    VA: "Virginia",
    WA: "Washington",
    WV: "West Virginia",
    WI: "Wisconsin",
    WY: "Wyoming",
  };
  // Convert full state name or abbreviation to abbreviation
  function getStateAbbreviation(state) {
    const tokens = state.split(/, |\n/);
    let newString = "";
    for (let i = 0; i < tokens.length; i++) {
      if (tokens[i] in stateAbbreviations) {
        newString += stateAbbreviations[tokens[i].toUpperCase()];
      } else {
        newString += tokens[i];
      }
      newString += " ";
    }
    return newString;
  }
  const filteredJobs = jobs.filter(
    (job) =>
      job[0].toLowerCase().includes(companySearch.toLowerCase()) &&
      (job[2].toLowerCase().includes(locationSearch.toLowerCase()) ||
        getStateAbbreviation(job[2])
          .toLowerCase()
          .includes(locationSearch.toLowerCase())) &&
      (tags.length === 0 || tags.includes(job[7]))
  );
  return (
    <div className="mainPage">
      <SearchBar
        onCompanyChange={handleCompanyChange}
        onLocationChange={handleLocationChange}
        addTag={addTag}
        removeTag={removeTag}
      />
      <JobBoard jobs={filteredJobs} />
    </div>
  );
}

export default Listing;
