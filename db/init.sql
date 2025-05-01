CREATE TABLE IF NOT EXISTS reddit_posts (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    score INTEGER,
    num_comments INTEGER,
    created_utc TIMESTAMP WITHOUT TIME ZONE,
    subreddit TEXT,
    url TEXT,
    is_self BOOLEAN,
    selftext TEXT
);
