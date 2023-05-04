import React from "react";
// import axios from "axios";
import ItemsComponent from "../components/ItemsComponent";

function Homepage(props) {
  return (
    <div>
      {/* <h1>Free Market</h1> */}
      <div className="search-container">
        <input placeholder="search items" className="search-input"></input>
        <button className="btn search-btn">Search</button>
      </div>
      <div className="items-container">
        <ItemsComponent />
      </div>
    </div>
  );
}

export default Homepage;
