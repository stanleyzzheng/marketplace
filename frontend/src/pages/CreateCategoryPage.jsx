import axios from "axios";
import { React, useState, useEffect } from "react";

function CreateCategoryPage() {
  // const [title, setTitle] = useState("");
  // const [description, setDescription] = useState("");

  const handleSubmit = async () => {
    const title = document.querySelector(".title").value;
    const description = document.querySelector(".description").value;
    console.log(title, description);

    const response = await axios.post("/api/categories/", {
      title: title,
      description: description,
    });
    console.log(response);

    // const response = await axios.post("/category");
  };
  return (
    <>
      <div className="page">
        <div>CreateCategoryPage</div>
        <div className="form-container">
          <label htmlFor="title">Title:</label>
          <input id="title" className="title" name="title"></input>
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            className="description"
            name="description"
          ></textarea>
          <button onClick={handleSubmit}>Submit</button>
        </div>
      </div>
    </>
  );
}

export default CreateCategoryPage;
