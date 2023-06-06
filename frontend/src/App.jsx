import { useState, useEffect } from "react";
import axios from "axios";
// import reactLogo from "./assets/react.svg";
// components
import Homepage from "./pages/HomePage";
import NavBar from "./components/NavBar";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// css imports
import "./App.css";
import "./card.css";
// page imports
import CategoryPage from "./pages/CategoryPage";
import ItemPage from "./pages/ItemPage";
import CreateCategoryPage from "./pages/CreateCategoryPage";
import AddItemPage from "./pages/AddItemPage";
import SignUpForm from "./forms/SignUpForm";
import LoginForm from "./forms/LoginForm";
import AddCatalogPage from "./pages/AddCatalogPage";
import CartPage from "./pages/CartPage";
// import getCookie from "./js/utils";
// import contexts
import { CartProvider } from "./contexts/CartContext";
function App() {
  // const [count, setCount] = useState(0);
  const [user, setUser] = useState(() => {
    const user = localStorage.getItem("user");
    console.log(user);

    return user;
  });
  // const [firstRender, setFirstRender] = useState(false);

  const checkAuth = async () => {
    // if (firstRender == true) return;
    const response = await axios.get("/api/who_am_i/");
    setUser(response.data.user);
    console.log(response.data);
    if (response.data.user) localStorage.setItem("user", response.data.user);

    axios.defaults.headers.common["Authorization"] = response.data["token"];
    // if (!firstRender && user == null) setFirstRender(true);
  };

  useEffect(() => {
    checkAuth();
  }, [user]);

  return (
    <div className="App">
      <Router>
        <CartProvider>
          {/* {firstRender && <NavBar user={user} />} */}
          <NavBar user={user} setUser={setUser} />

          <Routes>
            <Route path="/" element={<Homepage user={user} />} />
            <Route path="/addCatalog" element={<AddCatalogPage />} />
            <Route path="/categories" element={<CategoryPage />} />
            <Route path="/items" element={<ItemPage />} />
            <Route path="/addCategory" element={<CreateCategoryPage />} />
            <Route path="/addItem" element={<AddItemPage />} />
            <Route path="/signup" element={<SignUpForm setUser={setUser} />} />
            <Route path="/login" element={<LoginForm setUser={setUser} />} />
            <Route path="/cart" element={<CartPage />} />
          </Routes>
        </CartProvider>
      </Router>
    </div>
  );
}

export default App;
