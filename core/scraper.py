from bs4 import BeautifulSoup
import os

__author__='Pruthvi Kumar'
# 30 June 2019.
# pruthvikumar.123@gmail.com
# Scrape contents of a loaded webpage into a text file and store into a text file within sink.


class Scraper:

    def __init__(self, file_name):
        super(Scraper, self).__init__()
        self.file_name = file_name

    @staticmethod
    def __scrape_body(page_source):
        soup = BeautifulSoup(page_source)
        body = soup.find('body')
        the_contents_of_body_without_body_tags = body.findChildren()
        return the_contents_of_body_without_body_tags

    def extractor(self):
        try:
            # create a sink if not already existing
            os.makedirs('./../sink', exist_ok=True)

            # Extract page contents using Soup.
            with open("./../sink/{}.txt".format(self.file_name), "a") as f:
                print(self.__scrape_body(self.driver.page_source), file=f)

        except Exception as e:
            print('Failed to scrape contents into {} file. Stack trace to follow.'.format(self.file_name))
            print(str(e))
