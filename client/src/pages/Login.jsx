import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';

const Login = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
        credentials: 'include',
      });

      if (!response.ok) {
        throw new Error('Login failed');
      }

      const data = await response.json();
      localStorage.setItem('token', data.access_token);
      navigate('/dashboard');
    } catch (err) {
      setError('Invalid credentials. Please try again.');
    }
  };

  return (
    <div className="login-container">
      <div className="login-paper">
        <h1 className="login-title">AlphaNode Login</h1>
        {error && <div className="login-error">{error}</div>}
        <form className="login-form" onSubmit={handleSubmit}>
          <input
            className="form-field"
            type="email"
            id="email"
            name="email"
            placeholder="Email Address"
            required
            autoComplete="email"
            autoFocus
            value={formData.email}
            onChange={handleChange}
          />
          <input
            className="form-field"
            type="password"
            name="password"
            placeholder="Password"
            required
            autoComplete="current-password"
            value={formData.password}
            onChange={handleChange}
          />
          <button className="submit-button" type="submit">
            Sign In
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login; 