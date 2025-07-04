import React from 'react';
import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div className="container mt-5">
          <h1 className="display-4 text-center">Welcome to Octofit</h1>
          <img src={logo} className="App-logo" alt="logo" />
          <p className="lead text-center">
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <div className="text-center">
            <a
              className="btn btn-primary btn-lg"
              href="https://reactjs.org"
              target="_blank"
              rel="noopener noreferrer"
            >
              Learn React
            </a>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
