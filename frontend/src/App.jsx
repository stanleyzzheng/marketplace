import { useState, useEffect } from "react";
import axios from "axios";
// import reactLogo from "./assets/react.svg";
// components
import Homepage from "./pages/HomePage";
import NavBar from "./components/NavBar";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import CategoryPage from "./pages/CategoryPage";
import ItemPage from "./pages/ItemPage";
import CreateCategoryPage from "./pages/CreateCategoryPage";
import AddItemPage from "./pages/AddItemPage";
import SignUpForm from "./forms/SignUpForm";
import LoginForm from "./forms/LoginForm";
// import getCookie from "./js/utils";

function App() {
  // const [count, setCount] = useState(0);
  const [user, setUser] = useState(null);
  const [firstRender, setFirstRender] = useState(false);

  const checkAuth = async () => {
    const response = await axios.get("/api/who_am_i/");
    setUser(response.data.user);

    axios.defaults.headers.common["Authorization"] = response.data["token"];
    setFirstRender(true);
  };

  useEffect(() => {
    checkAuth();
  }, []);

  return (
    <div className="App">
      <Router>
        {firstRender && <NavBar user={user} />}

        <Routes>
          <Route path="/" element={<Homepage user={user} />} />
          <Route path="/addCatalog" element={<AddCatalogPage />} />
          <Route path="/categories" element={<CategoryPage />} />
          <Route path="/items" element={<ItemPage />} />
          <Route path="/addCategory" element={<CreateCategoryPage />} />
          <Route path="/addItem" element={<AddItemPage />} />
          <Route path="/signup" element={<SignUpForm />} />
          <Route path="/login" element={<LoginForm />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
