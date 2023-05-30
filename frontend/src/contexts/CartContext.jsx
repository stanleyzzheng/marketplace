import React, { createContext, useState, useEffect } from "react";
import axios from "axios";
const CartContext = createContext();

// Cart context provider component

const CartProvider = ({ children }) => {
  const [cartData, setCartData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchCartData = async () => {
    try {
      const response = await fetch("/api/cart/"); // Replace with your Django API endpoint URL
      const data = await response.json();
      console.log(data);

      setCartData(data);
      setIsLoading(false);
    } catch (error) {
      console.error(error);
    }
    // setIsLoading(false);
  };

  useEffect(() => {
    fetchCartData();
  }, [setCartData]);

  return (
    <CartContext.Provider value={[cartData, isLoading]}>
      {children}
    </CartContext.Provider>
  );
};

export { CartContext, CartProvider };
