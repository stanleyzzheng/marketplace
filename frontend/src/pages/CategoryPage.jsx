import React from "react";
import axios from "axios";
// import { useEffect } from "react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

// import getCookie from "../js/utils";

function CategoryPage() {
  const [categories, setCategories] = useState([]);

  const mapItems = (c) => {
    // if (!c.items) return;
    return c.items.map((item) => (
      // console.log(title);

      <li className="category-item">
        <Link>{item.title}</Link>${item.price}
      </li>
    ));
  };

  const mapCategory = (c) =>
    c.map((category) => {
      // console.log(category);
      return (
        <>
          <h1>{category.title}</h1>
          <ul>{mapItems(category)}</ul>
        </>
      );
    });

  const getCategories = async () => {
    try {
      // const csrftoken = getCookie("csrftoken");
      // axios.defaults.headers.common["X-CSRFToken"] = csrftoken;
      const response = await axios.get("/api/categories/");
      // console.log(response);

      setCategories(response.data);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getCategories();
  }, []);

  return (
    <>
      <div>CategoryPage</div>
      <div>{mapCategory(categories)}</div>
    </>
  );
}

export default CategoryPage;
