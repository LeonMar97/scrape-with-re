import re
from scrape_webz.data.Post import Post
from scrape_webz.scrapers.scraper_base import BaseScraper
from scrape_webz.utils.text_utils import clean_text
class Vbulletin(BaseScraper):
    '''should hold the url of file'''
    def parse_content(self, content):
        # content = content.replace('<br>', '')
        post_pat = r'<li data-node-id="\d+" .*?>(.*?)(?=<div class="post-signature.*?|<li data-node-id=.*?|<class="pagenav-container.*?>)'
        #excluded eaither the signature, or the nav if we are at the end, or the next li if there isnt a signature
        posts = re.findall(post_pat, content, re.DOTALL)

        title_ptn = r'<h2 class="b-post__title .*?>(.*?)</h2>'
        author_ptn = r'<span itemprop="name">(.*?)</span>'
        date_ptn= r'<div class="b-post__timestamp"><time itemprop="dateCreated" datetime=\'(.*?)\'>'
        content_ptn = r'itemprop="text">((?:<(?!div\b|/div\b)[^>]*>|<div[^>]*>.*?</div>|.)*?)</div>'

        def format_post(post)->dict:
            '''return the formated post as json'''
            title=self.found_or_none(title_ptn,post)
            author = self.found_or_none(author_ptn, post)
            date = self.found_or_none(date_ptn, post)
            content = self.found_or_none(content_ptn, post)
            content=clean_text(content)
            return Post(title, content, author, date).__dict__

        return {i + 1: format_post(post) for i, post in enumerate(posts)}
        #this is the full formated page
