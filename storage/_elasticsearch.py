from elasticsearch import Elasticsearch
import os

es = Elasticsearch("http://localhost:9200")

def index_post(post, index_name="reddit_posts"):
    es.index(index=index_name, document=post)

def create_index_if_not_exists(index_name="reddit_posts"):
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
