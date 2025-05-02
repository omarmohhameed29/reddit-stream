# processing/kafka_producer.py

from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_post(post, topic="reddit_posts"):
    """Sends a single post to Kafka."""
    producer.send(topic, value=post)

def flush_producer():
    """Flush remaining messages (optional, for graceful shutdown)."""
    producer.flush()
