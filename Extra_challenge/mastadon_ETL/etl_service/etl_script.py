import os
import requests
import psycopg2
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

load_dotenv()

MASTODON_URL = 'https://mastodon.social' # public 
TOPIC = "..." # Replace with any keywords to search posts on mastadon eg. 'bitcoin'
DISCORD_URL = os.getenv('DISCORD_WEBHOOK_URL')
THRESHOLD = 0.85 # sentiments are rated between -1 to 1 , replace with any number in this range

# Database connection details (from .env)
DB_DETAILS = {
    'host': os.getenv('ANALYTICS_DB_HOST'),
    'user': os.getenv('POSTGRES_USER_ANALYTICS'),
    'password': os.getenv('POSTGRES_PASSWORD_ANALYTICS'),
    'dbname': os.getenv('POSTGRES_DB_ANALYTICS')
}

ANALYZER = SentimentIntensityAnalyzer()
HTML_PATTERN = '...' # replace with a pattern to remove all HTML tags in the extracted text

# --- E: Extraction ---


def extract_data():
    """Gets the latest page of statuses from the Mastodon API."""
    api_url = f"{MASTODON_URL}/api/v1/timelines/tag/{TOPIC}"
    ...

# --- T: Transformation ---


def clean_html(raw_html):
    """Strips HTML tags and cleans whitespace."""
    ...

def transform_data(raw_statuses):
    """Cleans data, uses the raw timestamp string, and adds VADER sentiment."""
    transformed_list = []

    print("Transforming data by cleaning HTML and adding sentiment...")
    for status in raw_statuses:
        text_content = clean_html(status.get('content', ''))
        created_at_str = status.get('created_at')
        vs = ANALYZER.polarity_scores(text_content)

        transformed_list.append({
            'id': status.get('id'),
            'created_at': created_at_str, 
            'text_content': text_content,
            'vader_compound_score': vs['compound']
        })
    return transformed_list

# --- L: Load Analytics & Discord Integration ---


def connect_db():
    """
    Attempts to connect to the database
    """
    ...


def setup_tables(conn):
    """Create the analytics table with columns id,created_at,text_content,sentiment_score."""
    ...


def load_analytics_and_alert(analytics_conn, transformed_data):
    """Loads transformed data using ON CONFLICT DO NOTHING to avoid duplicate text."""

    query = """..."""
    # Map the data fields to the SQL placeholders based on their order.
    # (created_at, text_content, vader_compound_score)

    # Based on the transformed_data if any row has sentiment_score > THRESHOLD
    # send discord alert by calling send_discord_alert(data)
    ...

# --- Alerts to discord ---

def send_discord_alert(data):
    """Sends a message to Discord webhook."""
    message = {
        "content": f"**Positive Alert!** Score: {data['sentiment_score']:.2f} for #{TOPIC}",
        "embeds": [{"description": data['text_content']}]
    }
    requests.post(DISCORD_URL, json=message)


# --- Main pipeline function integrating ETL functions  ---

def run_etl_pipeline():
    """Executes the ETL pipeline."""
    # 1. connect_db()
    # 2. setup_tables()
    # 3. extract_data()
    # 4. transform_data()
    # 5. load_analytics_and_alert()
    ...


if __name__ == "__main__":
    run_etl_pipeline()
