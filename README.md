Idea for our project comes from: https://www.kaggle.com/datasets/andrewmvd/steam-reviews/code

Topic of the project: Language Sentiment in Game Reviews.
Aim: Create and deploy a model which will asses whether a certain review input as a string of characters has positive or negative sentiment. 

In our project we try to create a tool that can help in assesment of game reviews, based on a set of Steam Reviews regarding multiple games. For simplicity of the project only reviews in English and written using characters from Latin alphabet are taken into account. 

Model: In our project we use a simple LSTM.
Train data: For training we used majority of the data in the 'train_dataset.csv' file. Our data was divided into training set and testing set in the 9:1 proportions. In other words 90% of the data rows were taken into training and the rest into testing. Data is labelled.


