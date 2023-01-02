import axios from "axios";
import { React, useEffect, useState } from "react";

function AddItemPage() {
  const [categories, setCategories] = useState([]);

  const handleSubmit = async () => {
    const title = document.querySelector(".title").value;
    const description = document.querySelector(".description").value;
    const category = document.querySelector(".category").value;
    // console.log(category);

    const response = await axios
      .post("/api/items/", {
        title: title,
        description: description,
        category: category,
      })
      .then(() => {
        window.location.href = "/#/categories";
      });

    // const response = await axios.post("/category");
  };
  const request = async () => {
    const response = await axios.get("/api/categories/");
    // console.log(response.data);
    setCategories(response.data);
  };
  useEffect(() => {
    request();
  }, []);

  const mapCategories = () => {
    console.log(categories);

    return categories.map((category) => (
      <option value={category.id}>{category.title}</option>
    ));
  };

  return (
    <>
      <div className="page">
        <div>AddItemPage</div>
        <div className="form-container">
          <label htmlFor="title">Title:</label>
          <input className="title" id="title"></input>
          <label htmlFor="category">Category:</label>
          <select className="category" id="category">
            <option>------</option>
            {mapCategories()}
          </select>
          <label htmlFor="description">Description:</label>
          <textarea className="description" id="description"></textarea>
          <button onClick={handleSubmit}>Submit</button>
        </div>
      </div>
    </>
  );
}

export default AddItemPage;
