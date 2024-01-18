import os
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

# Function to remove stopwords
def remove_stopwords(text):
    return ' '.join(filter(lambda x: x not in st.session_state.nlp.Defaults.stop_words, text.split()))

# Function to lemmatize
def lemmatize(text):
    return ' '.join([x.lemma_ for x in st.session_state.nlp(text)])

def clean_data(data, re_letters):
    data['text'] = data['text'].apply(lambda x: x.lower())
    data['text'] = data['text'].apply(lambda x: re_letters.sub('', x))
    
    
if 'loaded_model' not in st.session_state:
    # loading the saved model
    model_path = os.path.join(os.path.dirname(os.getcwd()), 'model', '18_01_model.h5')
    loaded_model = load_model(model_path)
    st.session_state.loaded_model = loaded_model

if 'nlp' not in st.session_state:
    nlp = spacy.load('en_core_web_md', disable=['ner', 'parser'])
    nlp.add_pipe('sentencizer')
    nlp.Defaults.stop_words.add("game")
    nlp.Defaults.stop_words.add("play")
    nlp.Defaults.stop_words.add("t")
    st.session_state.nlp = nlp

if 'tokenizer' not in st.session_state:
    names=['text', 'label']
    df = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()), 'model', 'train_dataset.csv'), names=names)
    
    # clean data for tokenizer
    data=df[['text','label']]
    re_letters=re.compile(r"[^a-zA-Z\s']")

    clean_data(data, re_letters)
    data['text']=data['text'].apply(remove_stopwords)
    data['text']=data['text'].apply(lemmatize)

    tokenizer = Tokenizer(num_words=max_words)
    tokenizer.fit_on_texts(data.text)
    
    st.session_state.tokenizer = tokenizer

print('xdd')
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
    
    st.title('Review Sentiment Analysis')
    with st.form(key='game_review_form'):
        user_input = st.text_input("Enter a review: ")
        user_input = remove_stopwords(user_input)
        submit_button = st.form_submit_button(label='Submit')
    
    user_input = lemmatize(user_input)
    # Tokenize and pad the user input
    user_sequence = st.session_state.tokenizer.texts_to_sequences([user_input])
    user_data = pad_sequences(user_sequence, maxlen=max_len)
    
    # Make predictions for the user input
    user_prediction = st.session_state.loaded_model.predict(user_data)[0]
    
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