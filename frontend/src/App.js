// Importing modules
import React, { useState, useEffect } from "react";
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom";
import styles from "./App.css";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import About from "./pages/About/About";
import Home from "./pages/Home/Home";
import Register from "./pages/Register/Register";
import Login from "./pages/Login/Login";
import Dashboard from "./pages/Dashboard/Dashboard";

function App() {
	return (
		<div className="App">
			<BrowserRouter>
			<Navbar/>
				<div className="container">
					<Routes>
						<Route path="/" element={ <Home /> } />
						<Route path="/about" element={ <About /> } />
						<Route path="/login" element={ <Login /> } />
						<Route path="/register" element={ <Register /> } />
						<Route path="/dashboard" element={ <Dashboard /> } />
					</Routes>
				</div>
			<Footer />
			</BrowserRouter>
		
		</div>
	);
}

export default App;
