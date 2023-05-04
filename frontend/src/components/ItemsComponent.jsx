import React from "react";
import axios from "axios";
import { useEffect, useState } from "react";

function ItemCard({ item }) {
  return (
    <div className="card">
      <img src={item.image} alt={item.title} />
      <div className="card-body">
        <h5 className="card-title">{item.title}</h5>
        <p className="card-text">{item.description}</p>
        <p className="card-text">${item.price}</p>
        <a href="#" className="btn btn-primary">
          Buy now
        </a>
      </div>
    </div>
  );
}

function ItemsComponent() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get("/api/items/").then((res) => {
      setItems(res.data);
    });
  }, []);

  const mapItems = () =>
    items.map((item) => (
      <>
        {/* <h2>{item.title}</h2>
        <p>{item.description}</p>
        <p>${item.price}</p> */}
        <ItemCard item={item} />
      </>
    ));
  return <div>{mapItems()}</div>;
}

export default ItemsComponent;
