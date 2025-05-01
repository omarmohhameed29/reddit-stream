import praw
from datetime import datetime

reddit = praw.Reddit(site_name="dev")

def get_top_n_from_subreddit_limited_to_1000(subreddit, n):
    n = max(1000, n)
    for post in reddit.subreddit("business").hot(limit=5):
        print(f"Title: {post.title}")
        print(f"Author: {post.author.name if post.author else 'N/A'}")
        print(f"Text Content: {post.selftext}")
        print(f"Subreddit: {post.subreddit.display_name}")
        print(f"Score: {post.score}")
        print(f"Comments: {post.num_comments}")
        print(f"URL: {post.url}")
        print(f"Posted at: {datetime.utcfromtimestamp(post.created_utc)} UTC")
        print(f"Flair: {post.link_flair_text}")
        print("===")


