import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";

function CartComponent() {
  const [cartData, setCartData] = useState([]);

  const fetchCartData = async () => {
    try {
      const response = await axios.get("/cart/"); // Replace with your Django API endpoint URL
      setCartData(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    fetchCartData();
    console.log(cartData);
  }, []);

  return <div>Cart (10 items)</div>;
}

export default CartComponent;
