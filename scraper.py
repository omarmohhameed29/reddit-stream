import praw

reddit = praw.Reddit(site_name="dev")

# Example: Read public postsReddit()
subreddit = reddit.subreddit("technology")
for post in subreddit.hot(limit=5):
    print(post.title)
