import axios from "axios";
import { useNavigate } from "react-router-dom";

function SignUpForm(props) {
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("hello from submit");
    const password = document.getElementById("password").value;
    const username = document.getElementById("username").value;
    const verify = document.getElementById("verify-password").value;
    if (verify !== password) {
      alert("passwords must match");
      return;
    }

    const response = await axios
      .post("/api/signup/", {
        email: username,
        password: password,
      })
      .then(() => {
        navigate("/");
        window.location.reload();
        window.alert("Sign up succesful");
      })
      .catch((e) => {
        window.alert("Sign up unsuccessful");
        window.alert(e.request.responseText);
      });
    // console.log(response.data);
    // props.setUser(response.data.username);

    // localStorage.setItem("user", response.data.username);
  };
  return (
    <>
      <h1>Sign Up Form</h1>

      <div className="container">
        {/* create a form */}
        <form className="form" onSubmit={handleSubmit}>
          {/* Create a username label */}
          <label htmlFor="username">Username:</label>
          {/* Create a username field */}
          <input id="username" placeholder="username" type="email"></input>
          {/* Create a password label */}
          <label htmlFor="password">Password:</label>

          {/* Create a password field */}
          <input id="password" placeholder="password" type="password"></input>

          {/* Create a verify password label */}
          <label htmlFor="verify-password">Verify Password:</label>

          {/* Create a verify password field */}
          <input
            id="verify-password"
            placeholder="verify password"
            type="password"
          ></input>

          {/* Create a submit button */}
          <button className="btn">Sign up</button>
        </form>
      </div>
    </>
  );
}
export default SignUpForm;
