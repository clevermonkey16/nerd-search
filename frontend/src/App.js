import Listing from "./pages/Listing.js";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={<Listing />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
