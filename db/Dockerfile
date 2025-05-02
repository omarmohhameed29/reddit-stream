FROM python:3.12-slim

WORKDIR /app

# Install psycopg2 (PostgreSQL driver)
RUN pip install psycopg2-binary

# Copy only the necessary files
COPY db_client.py .

CMD ["python", "db_client.py"]
