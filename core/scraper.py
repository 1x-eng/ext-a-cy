__author__='Pruthvi Kumar'
# 30 June 2019.
# pruthvikumar.123@gmail.com
# Scrape contents of a given webpage (body) and extract into a flat file (.txt / .xml )

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

class LoadAndExtract:

    def __init__(self, url, file_name, dom_id, wait_time=5):
        super(LoadAndExtract, self).__init__()
        self.url = url
        self.file_name = file_name
        self.wait_time = wait_time
        self.dom_id = dom_id
        self.driver = webdriver.Chrome()

    @staticmethod
    def __scrape_body(page_source):
        soup = BeautifulSoup(page_source)
        body = soup.find('body')
        the_contents_of_body_without_body_tags = body.findChildren()
        return the_contents_of_body_without_body_tags

    def extractor(self):
        try:
            self.driver.get(self.url)

            # Wait as long as required, or maximum of 5 sec for element to appear
            # If successful, retrieves the element
            WebDriverWait(self.driver, self.wait_time).until(EC.presence_of_element_located((By.ID, self.dom_id)))

            # create a sink if not already existing
            os.makedirs('./../sink', exist_ok=True)

            # Extract page contents using Soup.
            with open("./../sink/{}.txt".format(self.file_name), "a") as f:
                print(self.__scrape_body(self.driver.page_source), file=f)

        except TimeoutError:
            print("Failed to load page / Failed to wait until {} element was loaded @ "
                  "{}.".format(self.dom_id, self.url))
        finally:
            self.driver.quit()


if __name__ == '__main__':
    g = LoadAndExtract('https://www.apricity.co.in', 'apricity', 'about')
    g.extractor()
