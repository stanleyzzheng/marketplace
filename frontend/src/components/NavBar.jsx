import React from "react";
import { Link } from "react-router-dom";

function NavBar() {
  return (
    <header className="header">
      <nav className="main-nav">
        <ul className="main-nav-list">
          <li>
            <Link className="link" to="/">
              Home
            </Link>
          </li>
          <li>
            <Link className="link" to="/categories">
              Categories
            </Link>
          </li>
          <li>
            <Link className="link" to="/items">
              All Items
            </Link>
          </li>
        </ul>
      </nav>
      <nav className="supplementary-nav">
        <ul className="supplementary-nav-list">
          <li>
            <Link className="link" to="/addItem">
              Add item
            </Link>
          </li>
          <li>
            <Link className="link" to="/addCategory">
              Add Category
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default NavBar;
