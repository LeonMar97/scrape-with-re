import re
from scrape_webz.data.Post import Post
from scrape_webz.scrapers.scraper_base import BaseScraper

class PhpbbScraper(BaseScraper):
    '''should hold the url of file'''
    def parse_content(self, content):
        content = content.replace('<br>', '')

        post_pat = r'<div id="p\d+" class="post has-profile bg\d">(.*?)(?=<div id="sig\d+" class="signature">|<div class="action-bar.*?>|<div id="p\d+".*?)'
        #capture incase user doesnt have signature, as well.
        posts = re.findall(post_pat, content, re.DOTALL)

        title_ptn = r'<div id="post_content\d+">.*?<a href="[^"]*">(.*?)</a>'
        author_ptn = r'<a.*?class="username.*?">(.*?)</a>'
        date_ptn = r'<time datetime="([^"]*)">'
        content_ptn = r'<div class="content">((?:<(?!div\b|/div\b)[^>]*>|<div[^>]*>.*?</div>|.)*?)</div>'

        def format_post(post)->dict:
            '''return the formated post as json, !!!!!!they are getting stripped in the found_or_non'''
            title=self.found_or_none(title_ptn,post)
            author = self.found_or_none(author_ptn, post)
            date = self.found_or_none(date_ptn, post)
            content = self.found_or_none(content_ptn, post)
            content = re.sub(r'<[^>]*>', '', content)
            return Post(title, content, author, date).__dict__

        return {i + 1: format_post(post) for i, post in enumerate(posts)}
        #this is the full formated page
