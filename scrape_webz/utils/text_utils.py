import re
from datetime import datetime

def clean_text(text):
    """Clean the text content by removing unwanted characters and HTML entities"""
    text = re.sub(
        r"&quote;", '"', text
    )  # Replace HTML entity &quote; with a double quote
    text = re.sub(r"&.*?;", "", text)  # Remove any remaining HTML entities
    text = re.sub(r"<[^>]*>", "", text)  # Remove any HTML tags
    text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with a single space
    return text

def format_date(input_date_str):
    input_date = datetime.strptime(input_date_str, "%Y-%m-%dT%H:%M:%S%z")
    return input_date.strftime("%Y/%m/%d %H:%M")