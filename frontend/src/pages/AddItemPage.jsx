import axios from "axios";
import { React, useEffect, useState } from "react";

function AddItemPage() {
  const [categories, setCategories] = useState([]);
  const [imageFile, setImageFile] = useState(null);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [category, setCategory] = useState("");

  const handleImageUpload = (event) => {
    setImageFile(event.target.files[0]);
  };

  const handleTitleChange = (event) => {
    setTitle(event.target.value);
  };

  const handleDescriptionChange = (event) => {
    setDescription(event.target.value);
  };

  const handlePriceChange = (event) => {
    setPrice(event.target.value);
  };

  const handleCategoryChange = (event) => {
    setCategory(event.target.value);
  };
  const handleSubmit = async () => {
    // const title = document.querySelector(".title").value;
    // const description = document.querySelector(".description").value;
    // const category = document.querySelector(".category").value;
    // const price = document.querySelector(".price").value;
    const formdata = new FormData();

    formdata.append("image", imageFile);
    formdata.append("title", title);
    formdata.append("description", description);
    formdata.append("price", price);
    formdata.append("category", category);

    console.log(category);

    const response = await axios
      .post("/api/items/", formdata)
      .then(() => {
        window.location.href = "/#/categories";
      })
      .catch((e) => {
        console.log(e);
      });

    // const response = await axios.post("/category");
  };
  const requestCategories = async () => {
    const response = await axios.get("/api/categories/");
    // console.log(response.data);
    setCategories(response.data);
  };
  useEffect(() => {
    requestCategories();
  }, []);

  const mapCategories = () => {
    console.log(categories);

    return categories.map((category) => (
      <option value={category.title}>{category.title}</option>
    ));
  };

  return (
    <>
      <div className="page">
        <div>AddItemPage</div>
        <div className="form-container">
          <label htmlFor="title">Title:</label>
          <input className="title" id="title" onChange={handleTitleChange} />
          <label htmlFor="image">Image:</label>
          <input type="file" onChange={handleImageUpload} />
          <label htmlFor="category">Category:</label>
          <select
            className="category"
            id="category"
            onChange={handleCategoryChange}
          >
            <option>------</option>
            {mapCategories()}
          </select>
          <label htmlFor="price">Price:</label>
          <input
            type="number"
            className="price"
            id="price"
            onChange={handlePriceChange}
          />
          <label htmlFor="description">Description:</label>
          <textarea
            className="description"
            id="description"
            onChange={handleDescriptionChange}
          ></textarea>

          <button onClick={handleSubmit}>Submit</button>
        </div>
      </div>
    </>
  );
}

export default AddItemPage;
