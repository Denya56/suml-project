// src/ReviewPrompt.js
import React, { useState } from 'react';
import '../styles/ReviewPrompt.css';

const ReviewPrompt = () => {
  const [reviewTitle, setReviewTitle] = useState('');
  const [reviewDescription, setReviewDescription] = useState('');

  const handleTitleChange = (e) => {
    setReviewTitle(e.target.value);
  };

  const handleDescriptionChange = (e) => {
    setReviewDescription(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Review Title:', reviewTitle);
    console.log('Review Description:', reviewDescription);
    // You can perform further actions with the review data here
  };

  return (
    <div className="review-card">
      <form className="review-form" onSubmit={handleSubmit}>
        <label htmlFor="titleInput" className="label">
          Review Title:
        </label>
        <input
          type="text"
          id="titleInput"
          className="input-field"
          value={reviewTitle}
          onChange={handleTitleChange}
        />

        <label htmlFor="descriptionInput" className="label">
          Review Description:
        </label>
        <textarea
          id="descriptionInput"
          className="text-area"
          value={reviewDescription}
          onChange={handleDescriptionChange}
        />

        <button type="submit" className="submit-button">
          Submit Review
        </button>
      </form>
    </div>
  );
};

export default ReviewPrompt;
