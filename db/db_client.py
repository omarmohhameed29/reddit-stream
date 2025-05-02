import psycopg2
from psycopg2 import sql
import os

def create_table_if_not_exists():
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="reddit_db",
        user="reddit_user",
        password="reddit_pass",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    
    # Query to check if the table exists
    check_table_exists_query = """
    SELECT EXISTS (
        SELECT 1 FROM information_schema.tables 
        WHERE table_name = 'reddit_posts'
    );
    """
    
    cur.execute(check_table_exists_query)
    table_exists = cur.fetchone()[0]
    
    if not table_exists:
        # Table doesn't exist, so create it
        create_table_query = """
            CREATE TABLE reddit_posts (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT,
                score INTEGER,
                num_comments INTEGER,
                created_utc TIMESTAMP WITHOUT TIME ZONE,
                subreddit TEXT,
                url TEXT,
                is_self BOOLEAN,
                selftext TEXT,
                sentiment TEXT,
                sentiment_score NUMERIC
            );
        """
        cur.execute(create_table_query)
        conn.commit()
        print("Table 'reddit_posts' created!")
    else:
        print("Table 'reddit_posts' already exists.")
    
    cur.close()
    conn.close()

def insert_post(post_data):
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="reddit_db",
        user="reddit_user",
        password="reddit_pass",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    
    # Insert query
    insert_query = """
    INSERT INTO reddit_posts (id, title, author, score, num_comments, created_utc, subreddit, url, is_self, selftext)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING;
    """
    
    # Execute the insert
    cur.execute(insert_query, post_data)
    conn.commit()
    print("Post inserted or already exists!")
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_table_if_not_exists()  # Check and create the table if necessary.
