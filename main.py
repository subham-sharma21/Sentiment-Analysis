from transformers import pipeline
import pandas as pd

# Load the pre-trained sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Example: Analyze a single sentence
text = "I love this new phone! The battery life is amazing."
result = sentiment_pipeline(text)
print("Single text result:", result)

# Example: Analyze a list of texts (e.g., customer reviews)
texts = [
    "I love this product! It's fantastic.",
    "Worst experience ever. Would not recommend.",
    "It's okay, nothing special.",
    "Absolutely wonderful service!",
    "Terrible quality, broke in a week."
]

results = sentiment_pipeline(texts)
for t, r in zip(texts, results):
    print(f"Text: {t}\nSentiment: {r['label']} (Confidence: {r['score']:.2f})\n")

# Optional: Analyze reviews from a CSV file
# Assume your CSV has a column named 'review'
# df = pd.read_csv('data/reviews.csv')
# reviews = df['review'].tolist()
# review_results = sentiment_pipeline(reviews)
# df['sentiment'] = [r['label'] for r in review_results]
# df.to_csv('data/reviews_with_sentiment.csv', index=False)
