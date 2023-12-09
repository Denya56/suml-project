import streamlit as st
import pandas as pd
import spacy
import pickle
from wordcloud import WordCloud
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tqdm import tqdm
import re
import seaborn as sns

max_words = 5000
max_len = 500

# loading the saved model
loaded_model = load_model('D:/Uni/7th sem/suml-project/model/modelv2.h5')

nlp = spacy.load('en_core_web_md', disable=['ner', 'parser'])
nlp.add_pipe('sentencizer')
nlp.Defaults.stop_words.add("game")
nlp.Defaults.stop_words.add("play")
nlp.Defaults.stop_words.add("t")

# Function to remove stopwords
def remove_stopwords(text):
    return ' '.join(filter(lambda x: x not in nlp.Defaults.stop_words, text.split()))

# Function to lemmatize
def lemmatize(text):
    return ' '.join([x.lemma_ for x in nlp(text)])
    
def main():
    
    tokenizer = Tokenizer(num_words=max_words)
    
    st.title('Diabetes Prediction Web App')
    user_input = st.text_input("Enter a review (or 'exit' to end): ")
    user_input = remove_stopwords(user_input)
    
    user_input = lemmatize(user_input)
    print(user_input)
    # Tokenize and pad the user input
    user_sequence = tokenizer.texts_to_sequences([user_input])
    user_data = pad_sequences(user_sequence, maxlen=max_len)
    print(user_input)
    print(user_data)
    
    # Make predictions for the user input
    user_prediction = loaded_model.predict(user_data)[0]
    
    # Print the predicted label for the user input
    if user_prediction[1] > user_prediction[0]:
        predicted_label = 1
    else:
        predicted_label = 0
    
    print("Predicted Label:", predicted_label)


if __name__ == '__main__':
    main()