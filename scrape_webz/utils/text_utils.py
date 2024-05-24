import re
def clean_text(text):
        '''Clean the text content by removing unwanted characters and HTML entities'''
        text = re.sub(r'&quote;', '"', text)   # Replace HTML entity &quote; with a double quote
        text = re.sub(r'&.*?;', '', text)      # Remove any remaining HTML entities
        text = re.sub(r'<[^>]*>', '', text)    # Remove any HTML tags
        text = re.sub(r'\s+', ' ', text)       # Replace multiple spaces with a single space
        return text      