import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Authentication/Login';
import OlmsDashboard from './components/OLMS/OlmsDashboard';

function App() {
  const user = localStorage.getItem('authToken');

  return (
    <Router>
      <Routes>
        {/* If user is logged in, render OlmsDashboard, otherwise redirect to Login */}
        {user ? (
          <Route path="/dashboard" element={<OlmsDashboard />} />
        ) : (
          <Route path="*" element={<Navigate to="/login" />} />
          )}
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;
