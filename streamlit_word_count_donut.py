import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Download and cache the CSV file from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/kohchingay/greek_bible/main/01-matthew.csv"
    df = pd.read_csv(url)
    # Standardize word column for matching (strip whitespace, uppercase)
    df['word'] = df['word'].astype(str).str.strip().str.upper()
    return df

df = load_data()

st.title("Greek Bible Word Frequency Donut Chart")
st.write("Enter a (Greek) word to see its frequency as a proportion of total words.")

user_word = st.text_input("Enter word (case-insensitive, Greek):", "")

if user_word:
    search_word = user_word.strip().upper()
    word_count = (df['word'] == search_word).sum()
    total_words = len(df)
    other_count = total_words - word_count

    fig = go.Figure(data=[go.Pie(
        labels=[f"'{user_word}'", "Other Words"],
        values=[word_count, other_count],
        hole=0.6,
        textinfo='label+percent',
        marker=dict(colors=['#636efa', '#e5ecf6'])
    )])
    fig.update_layout(
        title_text=f"Frequency of '{user_word}' in 01-matthew.csv ({word_count}/{total_words})",
        annotations=[dict(text=f"{word_count}/{total_words}", x=0.5, y=0.5, font_size=20, showarrow=False)]
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Please enter a word to see its frequency.")