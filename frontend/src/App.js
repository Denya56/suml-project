// src/App.js
import React from 'react';
import ReviewPrompt from './components/ReviewPrompt';
import './App.css'; // Import the CSS file for additional styling

function App() {
  return (
    <div className="app-container">
      <h1 className="app-title">Review Sentiment Analysis</h1>
      <ReviewPrompt />
    </div>
  );
}

export default App;
