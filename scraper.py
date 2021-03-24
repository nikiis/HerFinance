import requests
from bs4 import BeautifulSoup
import pprint
import json


class Scraper:
    def __init__(self, website):
        self.website_path = website
        self.info = []

    def parse(self):
        page = BeautifulSoup(requests.get(self.website_path).content, "html.parser")

        for section in page.select('div .single-result-story'):
            self.info.append({'heading': section.find('h5').text,
                              'image': section.find('img')['src'],
                              'contributor': {'name': section.select_one('p a').text,
                                              'link': section.select_one('p a')['href']},
                              'description': section.select_one('p > p:nth-child(2)').text.strip(),
                              'article': f"https://www.londonstockexchange.com{section.select_one('div > a')['href']}"})

        return self.info


if __name__ == "__main__":
    scraper = Scraper('https://www.londonstockexchange.com/personal-investing-hub?exploreStoriesFilters=589')
    pp = pprint.PrettyPrinter(indent=4)
    # print(scraper.parse())
    with open('articles.json', mode='w') as f:
        json.dump(scraper.parse(), f)

    # pp.pprint(scraper.parse())
