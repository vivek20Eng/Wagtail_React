import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post("http://localhost:8000/api/login/", {
        username: username,
        password: password,
      })
      .then((response) => {
        console.log(response.data.message);
        navigate("/dashboard");
      })
      .catch((error) => {
        console.error("Login failed:", error.response.data.error);
      });
  };

  return (
    <div className="mainContainer">
      <div className="titleContainer">
        <div>Login</div>
      </div>
      <br />
      <form onSubmit={handleSubmit}>
        <div className="inputContainer">
          <input
            value={username}
            placeholder="Enter your email here"
            onChange={(e) => setUsername(e.target.value)}
            className="inputBox"
          />
        </div>
        <br />
        <div className="inputContainer">
          <input
            value={password}
            placeholder="Enter your password here"
            onChange={(e) => setPassword(e.target.value)}
            className="inputBox"
            type="password"
          />
        </div>
        <br />
        <div className="inputContainer">
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  );
};

export default Login;
