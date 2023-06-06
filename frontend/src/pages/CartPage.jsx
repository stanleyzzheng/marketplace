import axios from "axios";
import { React, useContext, useEffect, useState } from "react";
import { CartContext } from "../contexts/CartContext";
import "../cart.css";

function CartPage() {
  const [cartData, isLoading] = useContext(CartContext);
  console.log(cartData);

  return (
    <div className="cart-page">
      <h1>Cart</h1>
      <ul className="cart-items">
        {cartData.map((item) => (
          <li key={item.id} className="cart-item">
            <img
              src={item.item.image}
              alt={item.item.title}
              className="item-image"
            />
            <div className="item-details">
              <span className="item-name">{item.item.title}</span>
              <span className="item-price">${item.item.price}</span>
              <span className="item-quantity">Quantity: {item.quantity}</span>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CartPage;
