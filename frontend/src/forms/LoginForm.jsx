import axios from "axios";
import { useNavigate } from "react-router-dom";

function LoginForm(props) {
  const navigate = useNavigate();
  const handleSubmit = async (e) => {
    e.preventDefault();
    // console.log("hello from submit");
    const password = document.getElementById("password").value;
    const username = document.getElementById("username").value;

    const response = await axios.post("/api/login/", {
      email: username,
      password: password,
    });

    // console.log(response.data);

    // console.log(props);
    // props.setUser(response.data.user);
    // localStorage.setItem("user", response.data.user);

    navigate("/");
    window.location.reload();
  };
  return (
    <>
      <h1>Log In Form</h1>

      <div className="container">
        {/* create a form */}
        <form className="form" onSubmit={handleSubmit}>
          {/* Create a username label */}
          <label htmlFor="username">Username:</label>
          {/* Create a username field */}
          <input id="username" placeholder="username"></input>
          {/* Create a password label */}
          <label htmlFor="password">Password:</label>

          {/* Create a password field */}
          <input id="password" placeholder="password"></input>

          {/* Create a submit button */}
          <button className="btn">Log in</button>
        </form>
      </div>
    </>
  );
}
export default LoginForm;
