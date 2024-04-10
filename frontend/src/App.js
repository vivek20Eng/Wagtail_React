import React from 'react';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"; 

import Login from './components/Authentication/Login';
import OlmsDashboard from './components/OLMS/OlmsDashboard';

function App() {
  return (
    <Router>
      <Routes> 
        <Route path="/dashboard" element={<OlmsDashboard />} /> 
        <Route path="/" element={<Login />} /> 
      </Routes>
    </Router>
  );
}

export default App;
