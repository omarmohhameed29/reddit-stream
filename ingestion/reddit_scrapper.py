import praw
from datetime import datetime
import json
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from processing.kafka_producer import publish_post  # Import the Kafka producer

reddit = praw.Reddit(site_name="dev")

last_run_file = "last_run.json"
if os.path.exists(last_run_file):
    with open(last_run_file) as f:
        last_run = json.load(f)["last_timestamp"]
else:
    last_run = 0  # start from the beginning

def get_top_new_n_from_subreddit_limited_to_1000(subreddit, n):
    n = min(1000, n)
    new_last_run = last_run
    collected_posts = []

    for post in reddit.subreddit(subreddit).new(limit=n):
        if post.created_utc > last_run:
            post_data = {
                "id": post.id,
                "title": post.title,
                "author": post.author.name if post.author else "N/A",
                "text": post.selftext,
                "subreddit": post.subreddit.display_name,
                "score": post.score,
                "num_comments": post.num_comments,
                "created_utc": post.created_utc,
                "flair": post.link_flair_text,
                "url": post.url,
                "is_self": post.is_self,
            }
            collected_posts.append(post_data)

            # Send the post to Kafka as a producer
            publish_post(post_data)

            if post.created_utc > new_last_run:
                new_last_run = post.created_utc

    try:
        # Save the new last timestamp
        with open(last_run_file, "w") as f:
            json.dump({"last_timestamp": new_last_run}, f)
            print("Last timestamp updated.")
    except Exception as e:
        print(f"Error saving last run timestamp: {e}")

    return collected_posts

if __name__ == "__main__":
    posts = get_top_new_n_from_subreddit_limited_to_1000("technology", 1000)
    print(len(posts))
