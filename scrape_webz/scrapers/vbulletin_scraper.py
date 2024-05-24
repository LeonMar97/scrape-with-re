import re
from scrape_webz.data.Post import Post
from scrape_webz.scrapers.scraper_base import BaseScraper

class Vbulletin(BaseScraper):
    '''should hold the url of file'''
    def parse_content(self, content):
        content = content.replace('<br>', '')

        post_pat = r'<li data-node-id="\d+" .*?>(.*?)(?=<div class="post-signature.*?|<li data-node-id=.*?|<class="pagenav-container.*?>)'
        #excluded eaither the signature, or the nav if we are at the end, or the next li if there isnt a signature
        posts = re.findall(post_pat, content, re.DOTALL)

        title_ptn = r'<div id="post_content\d+">.*?<a href="[^"]*">(.*?)</a>'
        author_ptn = r'<a.*?class="username.*?">(.*?)</a>'
        date_ptn = r'<time datetime="([^"]*)">'
        content_ptn = r'<div class="content">((?:<(?!div\b|/div\b)[^>]*>|<div[^>]*>.*?</div>|.)*?)</div>'

        def format_post(post)->dict:
            '''return the formated post as json'''
            title = re.search(title_ptn, post, re.DOTALL).group(1)
            author = re.search(author_ptn, post, re.DOTALL).group(1)
            date = re.search(date_ptn, post, re.DOTALL).group(1)
            content = re.search(content_ptn, post, re.DOTALL).group(1)
            content = re.sub(r'<[^>]*>', '', content)
            return Post(title, content, author, date).__dict__

        return {i + 1: format_post(post) for i, post in enumerate(posts)}
        #this is the full formated page
