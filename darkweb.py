import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')

# Sample Data Loading
def load_data():
    data = {
        'date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
        'message': ["Buy cheap CC dumps now!" if i % 2 == 0 else "Earn BTC fast, click here!" for i in range(100)]
    }
    return pd.DataFrame(data)

# Tokenization & Keyword Extraction
def extract_keywords(messages):
    words = []
    for msg in messages:
        words.extend(word_tokenize(msg.lower()))
    common_words = Counter(words).most_common(20)
    return dict(common_words)

# Visualization - Word Cloud
def generate_wordcloud(word_freq):
    wc = WordCloud(width=800, height=400, background_color='black').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

# Streamlit App
st.title("🕵️ Dark Web Spam Trend Analysis")

data = load_data()

# Show raw data
st.subheader("📊 Raw Spam Data")
st.dataframe(data.head())

# Spam Trends Over Time
st.subheader("📈 Spam Activity Over Time")
data['date'] = pd.to_datetime(data['date'])
data['count'] = 1
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='date', y='count', data=data.groupby('date').count(), ax=ax)
st.pyplot(fig)

# Keyword Analysis
st.subheader("🔍 Common Spam Keywords")
word_freq = extract_keywords(data['message'])
st.bar_chart(pd.DataFrame(word_freq.items(), columns=['Keyword', 'Frequency']).set_index('Keyword'))

# Word Cloud
st.subheader("🌍 Word Cloud Representation")
generate_wordcloud(word_freq)

st.markdown("Developed by [Your Name]")
