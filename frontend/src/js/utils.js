import axios from "axios";
// import { useEffect } from "react";

export default function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }

  // const curr_user = async () => {
  //   let myResponse = await axios.get("current_user");
  //   let user =
  //     myResponse.data && myResponse.data[0] && myResponse.data[0].fields;
  //   setUser(user);
  // };
  // useEffect(() => {
  //   curr_user();
  // }, []);

  return cookieValue;
}

// const csrftoken = getCookie("csrftoken");
// axios.defaults.headers.common["X-CSRFToken"] = csrftoken;
