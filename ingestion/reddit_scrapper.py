import praw
from datetime import datetime
import json
import os

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

    for post in reddit.subreddit(subreddit).new(limit=n):
        if post.created_utc > last_run:
            print(f"Title: {post.title}")
            print(f"Author: {post.author.name if post.author else 'N/A'}")
            print(f"Text Content: {post.selftext}")
            print(f"Subreddit: {post.subreddit.display_name}")
            print(f"Score: {post.score}")
            print(f"Comments: {post.num_comments}")
            print(f"Posted at: {datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
            print(f"Flair: {post.link_flair_text}")
            print(f"URL: {post.url}")
            print("===")
            if post.created_utc > new_last_run:
                new_last_run = post.created_utc

    try:
        # Save the new last timestamp
        with open(last_run_file, "w") as f:
            json.dump({"last_timestamp": new_last_run}, f)
            print("Last timestamp updated.")
    except Exception as e:
        print(f"Error saving last run timestamp: {e}")
    print("===")

