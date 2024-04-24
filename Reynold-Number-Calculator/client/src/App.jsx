import "./App.css";
import { Route, BrowserRouter, Routes } from "react-router-dom";

import Header from "./components/header/Header.jsx";
import Navbar from "./components/navbar/Navbar.jsx";
import Footer from "./components/footer/Footer.jsx";

import Home from "./pages/home/Home.jsx";
import NotFound from "./pages/notfound/NotFound.jsx";


function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Header />
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="*" element={<NotFound />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
