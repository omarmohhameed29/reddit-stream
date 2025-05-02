# 🧠 Reddit Sentiment Analyzer (Data Engineering Project)

This is a full-stack data engineering project that ingests Reddit posts, streams them via Kafka, performs sentiment analysis, stores the results in PostgreSQL and Elasticsearch, and visualizes them with Kibana. The system is orchestrated using Docker.

## 📚 Table of Contents
- [🚀 Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📦 Project Structure](#-project-structure)
- [⚙️ How to Run](#️-how-to-run)
- [📈 Visualizations](#-visualizations)
- [🏗️ Architecture](#️-architecture)
- [📋 Future Improvements](#-future-improvements)

## Features
- ✅ Scrape real-time Reddit data using PRAW.
- ✅ Publish Reddit posts to Kafka.
- ✅ Consume posts and perform sentiment analysis.
- ✅ Store enriched posts in PostgreSQL and Elasticsearch.
- ✅ Visualize sentiment trends with Kibana dashboards.
- ✅ Orchestrate everything via Docker.

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Ingestion | Python, PRAW |
| Stream Processing | Apache Kafka + Zookeeper |
| Storage | PostgreSQL, Elasticsearch |
| Analysis | TextBlob (Sentiment Analysis) |
| Visualization | Kibana |
| Orchestration | Docker, Docker Compose |

## 📦 Project Structure

```
reddit-sentiment-analyzer/
├── db/            # DB client to create schema
├── docker/        # Docker files and environment
├── ingestion/     # Reddit scraper
├── processing/    # Sentiment analysis + Kafka consumer
├── storage/       # Elasticsearch indexing
├── monitoring/    # Kibana/Grafana dashboards
├── tests/         # Unit tests
├── docker-compose.yml
├── README.md
└── requirements.txt
```

## ⚙️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/reddit-sentiment-analyzer.git
cd reddit-sentiment-analyzer
```

### 2. Build and start containers
```bash
docker-compose up -d --build
```

This will spin up:
- PostgreSQL
- Kafka & Zookeeper
- Elasticsearch
- Kibana
- Kafka Consumer (auto-starts)
- DB Client (to create the table)

### 3. Run the Reddit Scraper (Kafka Producer)
In a separate terminal:
```bash
docker exec -it <your-container> bash
# or if you're running locally with a venv:
source venv/bin/activate
python ingestion/reddit_scraper.py
```

This script pulls Reddit posts and sends them to Kafka.

### 4. Access Kibana Dashboard
Visit http://localhost:5601 and:
- Navigate to Stack Management > Index Patterns
- Create a new pattern matching your Elasticsearch index (e.g., `reddit-posts-*`)
- Visualize your data in Discover or Dashboard

## 📈 Visualizations

You can create a Kibana dashboard to show:
- Sentiment score trends over time
- Most active subreddits
- Word cloud of positive/negative posts
- Post volume per hour/day

Optional: use `monitoring/kibana_dashboard.json` to import a prebuilt dashboard.

![Sentiment Dashboard](/images/kibana-dashboard.png)

*Sample visualization of sentiment analysis results from Reddit data*

## 🏗️ Architecture

![Project Architecture](/images/architecture.png)

*The architecture diagram shows the data flow from Reddit through Kafka to storage and visualization.*

## 📋 Future Improvements

- Integrate Grafana for PostgreSQL-based visualizations
- Improve sentiment analysis with VADER or BERT
- Store raw and cleaned text separately
- Add test coverage and CI/CD pipelines
- Add scheduling capabilities for periodic data ingestion

## 🧠 Author
Made with ❤️ by [Your Name]