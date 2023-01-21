import React from "react";
import axios from "axios";

function Homepage(props) {
  return (
    <div>
      <h1>Hello, {props.user} :)</h1>
      {/* <button>Sign Up</button>
      <button>Login</button>
      <button>Log Out</button> */}
    </div>
  );
}

export default Homepage;
