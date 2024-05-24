from scrape_webz.scrapers.phpbb_scraper import PhpbbScraper
from scrape_webz.utils.file_utils import save_to_json


def main():
    url = 'https://www.phpbb.com/community/viewtopic.php?f=46&t=2159437'
    scraper = PhpbbScraper(url)
    '''current website scrapped'''
    data = scraper.scrape()
    '''current data to save'''
    f='phpbb_web.txt'
    '''current file'''
    save_to_json(f,data)

if __name__ == "__main__":
    main()