import axios from "axios";
import React from "react";
import { Link, useNavigate } from "react-router-dom";

// import { SignUpButton, LoginButton } from "./Buttons";

function SignUpButton() {
  return (
    <Link className="link" to="/signup">
      Sign Up
    </Link>
  );
}

function LoginButton() {
  return (
    <Link className="link" to="/login">
      Log In
    </Link>
  );
}

function LogOutButton() {
  const navigate = useNavigate();

  const handleLogOut = async () => {
    const response = await axios.post("/api/logout/");
    console.log(response);
    navigate("/");
    window.location.reload();
  };
  return (
    <Link className="link" onClick={handleLogOut}>
      Log Out
    </Link>
  );
}

function LoggedInNavBar() {
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
          <li>
            <LogOutButton />
          </li>
        </ul>
      </nav>
    </>
  );
}

function NavBar(props) {
  return props.user ? (
    <header className="header">
      <LoggedInNavBar />
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
          <li>
            <SignUpButton />
          </li>
          <li>
            <LoginButton />
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default NavBar;
