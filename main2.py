from transformers import pipeline

# Load the pre-trained sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

while True:
    text = input("Enter a sentence for sentiment analysis (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        break
    result = sentiment_pipeline(text)[0]
    print(f"Sentiment: {result['label']} (Confidence: {result['score']:.2f})\n")
