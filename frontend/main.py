import streamlit as st
import pandas as pd
import spacy
import pickle
from wordcloud import WordCloud
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from tqdm import tqdm
import re
import seaborn as sns

max_words = 5000
max_len = 500

# loading the saved model
loaded_model = load_model('..\model\modelv2.h5')

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
    st.markdown("""
    <style>
    .block-container {
        background-color: #000000;
        color: #00ff00;
        font-family: Courier New;
    }
    .st-emotion-cache-10trblm {
        color: #00ff00;
        text-align: center;
    }
    p {
        color: #00ff00;
        text-align: center;
    }
    .stTextArea textarea {
        background-color: #333333;
        color: #00ff00;
    }
    .stButton>button {
        color: #00ff00;
        background-color: #333333;
    }
    </style>
    """, unsafe_allow_html=True)

    tokenizer = Tokenizer(num_words=max_words)
    
    st.title('Review Sentiment Analysis')
    with st.form(key='game_review_form'):
        user_input = st.text_input("Enter a review: ")
        user_input = remove_stopwords(user_input)
        submit_button = st.form_submit_button(label='Submit')
    
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
    if submit_button:
        if predicted_label == 1:
            st.write(f"Predicted label: Positive")
        elif predicted_label == 0:
            st.write(f"Predicted label: Negative")


if __name__ == '__main__':
    main()