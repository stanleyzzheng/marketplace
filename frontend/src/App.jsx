// import { useState } from "react";
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
// import getCookie from "./js/utils";

function App() {
  // const [count, setCount] = useState(0);

  return (
    <div className="App">
      <Router>
        <NavBar />

        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/categories" element={<CategoryPage />} />
          <Route path="/items" element={<ItemPage />} />
          <Route path="/addCategory" element={<CreateCategoryPage />} />
          <Route path="/addItem" element={<AddItemPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
