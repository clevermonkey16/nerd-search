import Home from "./pages/Home.js";
import Listing from "./pages/Listing.js";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={<Home />}></Route>
        <Route
          path="/listing"
          element={<Listing />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
