from scrape_webz.scrapers.phpbb_scraper import PhpbbScraper
from scrape_webz.utils.file_utils import save_to_json
from scrape_webz.scrapers.vbulletin_scraper import Vbulletin

def main():
    url = 'https://www.phpbb.com/community/viewtopic.php?f=46&t=2159437'
    url='https://forum.vbulletin.com/forum/vbulletin-3-8/vbulletin-3-8-questions-problems-and-troubleshooting/414325-www-vs-non-www-url-causing-site-not-to-login'
    # scraper = PhpbbScraper(url)
    scraper = Vbulletin(url)

    '''current website scrapped'''
    data = scraper.scrape()
    '''current data to save'''
    f='phpbb_web.txt'
    '''current file'''
    save_to_json(f,data)

if __name__ == "__main__":
    main()