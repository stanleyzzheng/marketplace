import React from "react";
import { useContext } from "react";
import { CartContext } from "../contexts/CartContext";
function CartComponent() {
  const [cartData, isLoading] = useContext(CartContext);
  // const [cartData, setCartData] = useState([]);

  // const fetchCartData = async () => {
  //   try {
  //     const response = await axios.get("/api/cart/"); // Replace with your Django API endpoint URL

  //     setCartData(response.data);
  //   } catch (error) {
  //     console.error(error);
  //   }
  // };

  // useEffect(() => {
  //   fetchCartData();
  // }, []);

  return !isLoading ? <div>Cart ({cartData.length})</div> : "";
  // return <div>Cart ({cartData.length})</div>;
}

export default CartComponent;
