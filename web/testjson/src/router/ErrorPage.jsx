import React from "react";
import { useNavigate } from "react-router-dom";

const ErrorPage = () => {
  const navigate = useNavigate();
  return (
    <>
      <h1>404 - Page Not Found</h1>
      <button onClick={() => navigate("/")}>Go Home</button>
      <button onClick={() => navigate(-1)}>Go Back</button>
    </>
  );
};

export default ErrorPage;
