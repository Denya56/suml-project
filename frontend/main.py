import streamlit as st

def game_review_form():
    st.title("Review Sentiment Analysis")

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

    with st.form(key='game_review_form'):
        game_review = st.text_area("Game Review")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write(f"Game Review: {game_review}")

if __name__ == "__main__":
    game_review_form()