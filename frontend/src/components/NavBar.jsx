import React from "react";
import { Link } from "react-router-dom";
// import { SignUpButton, LoginButton } from "./Buttons";

function SignUpButton() {
  return (
    <Link className="btn" to="/signup">
      Sign Up
    </Link>
  );
}

function LoginButton() {
  return (
    <Link className="btn" to="/login">
      Log In
    </Link>
  );
}

function navbar() {
  return (
    <>
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
    </>
  );
}

function NavBar(props) {
  return props.authenticated ? (
    <header className="header">
      <navbar />
    </header>
  ) : (
    <header className="header">
      <nav className="main-nav">
        <ul className="main-nav-list">
          <li>
            <Link className="link" to="/">
              Home
            </Link>
          </li>
        </ul>
      </nav>
      <nav>
        <ul className="supplementary-nav-list">
          <li className="link" to="/signup">
            <SignUpButton />
          </li>
          <li className="link" to="/login">
            <LoginButton />
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default NavBar;
