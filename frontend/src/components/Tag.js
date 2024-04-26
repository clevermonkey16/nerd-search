import React from "react";

const Tag = ({ tag, onRemove }) => {
  const handleRemove = () => {
    onRemove(tag);
  };

  return (
    <div className="tag">
      <span>{tag}</span>
      <button onClick={handleRemove}>X</button>
    </div>
  );
};

export default Tag;
