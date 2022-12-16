import axios from "axios";
import React from "react";
import { useEffect, useState } from "react";

function ItemPage() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get("/api/items/").then((res) => {
      setItems(res.data);
    });
  }, []);

  const mapItems = () => items.map((item) => <p>{item.title}</p>);

  return (
    <div>
      <h3>Item Page</h3>
      {mapItems()}
    </div>
  );
}

export default ItemPage;
