from kafka import KafkaConsumer
import json
from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db_client import insert_post  # Function to insert posts into PostgreSQL
from sentiment_analysis import analyze_sentiment

consumer = KafkaConsumer(
    'reddit_posts',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='sentiment-consumer-group'
)

def process_post(post):
    title = post.get("title", "")
    text = post.get("text", "")
    full_text = f"{title}\n{text}"

    sentiment, score = analyze_sentiment(full_text)

    print(f"---\nSubreddit: {post.get('subreddit')}")
    print(f"Title: {title}")
    print(f"Sentiment: {sentiment} (score: {score})")
    print(f"Posted at: {datetime.utcfromtimestamp(post['created_utc']).strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print("===")

    # Insert post data with sentiment into PostgreSQL
    insert_post(post, sentiment, score)

def consume():
    print("Kafka consumer started. Listening to 'reddit_posts'...")
    for message in consumer:
        post = message.value
        process_post(post)

if __name__ == "__main__":
    consume()
