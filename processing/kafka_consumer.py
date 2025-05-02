from kafka import KafkaConsumer
import json
from sentiment_analysis import analyze_sentiment
from datetime import datetime

# Set up Kafka consumer
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

    # You could add logic here to insert the post + sentiment into a PostgreSQL DB

def consume():
    print("Kafka consumer started. Listening to 'reddit_posts'...")
    for message in consumer:
        post = message.value
        process_post(post)

if __name__ == "__main__":
    consume()
