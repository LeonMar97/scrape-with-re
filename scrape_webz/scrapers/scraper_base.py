import re
class BaseScraper:
    def __init__(self, url):
        self.url = url
    
    def fetch_content(self):
        import requests
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text
    
    def parse_content(self, content)->dict:
        '''should return the full page parsed as devided posts objects'''
        raise NotImplementedError("Subclasses should implement this method")
    
    def scrape(self):
        content = self.fetch_content()
        return self.parse_content(content)

    def found_or_none(self,pattern,post):
        cur=re.search(pattern, post, re.DOTALL)
        return cur.group(1).strip() if cur else "not found"