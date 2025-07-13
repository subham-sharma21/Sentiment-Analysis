import streamlit as st
from transformers import pipeline

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        font-size:2.5em;
        font-weight:bold;
        color:#4F8BF9;
        text-align:center;
        margin-bottom:10px;
    }
    .subtitle {
        color:#666666;
        text-align:center;
        font-size:1.2em;
        margin-bottom:30px;
    }
    .sentiment-positive {
        color: #27ae60;
        font-size: 1.5em;
        font-weight: bold;
    }
    .sentiment-negative {
        color: #e74c3c;
        font-size: 1.5em;
        font-weight: bold;
    }
    .sentiment-neutral {
        color: #f1c40f;
        font-size: 1.5em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Explicitly specify the model for sentiment analysis
@st.cache_resource
def load_pipeline():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

sentiment_pipeline = load_pipeline()

st.markdown('<div class="main-title">Sentiment Analysis App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter a sentence to analyze its sentiment (positive or negative).</div>', unsafe_allow_html=True)

user_input = st.text_area("Your text here:", "")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        with st.spinner("Analyzing sentiment..."):
            result = sentiment_pipeline(user_input)[0]
            label = result["label"]
            score = result["score"]

        # Color the sentiment output
        if label == "POSITIVE":
            st.markdown(f'<div class="sentiment-positive">Sentiment: {label} 🎉</div>', unsafe_allow_html=True)
            st.balloons()
        elif label == "NEGATIVE":
            st.markdown(f'<div class="sentiment-negative">Sentiment: {label} 😞</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="sentiment-neutral">Sentiment: {label} 😐</div>', unsafe_allow_html=True)

        st.write(f"**Confidence:** {score:.2f}")
    else:
        st.warning("Please enter some text to analyze.")
