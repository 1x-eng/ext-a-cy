from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

__author__='Pruthvi Kumar'
# 30 June 2019.
# pruthvikumar.123@gmail.com
# Load web-page associated with given URL and await given dom element until specified time.


class LoadPage:

    def __init__(self, url, dom_id, wait_time=5):
        super(LoadPage, self).__init__()
        self.url = url
        self.dom_id = dom_id
        self.wait_time = wait_time
        self.driver = webdriver.Chrome()

    def extractor(self):
        try:
            self.driver.get(self.url)

            # Wait as long as required, or maximum of 5 sec for element to appear
            # If successful, retrieves the element
            WebDriverWait(self.driver, self.wait_time).until(EC.presence_of_element_located((By.ID, self.dom_id)))

            # If you wanted to do any activity like login etc., conduct that here.

            return self.driver.page_source

        except TimeoutError:
            print("Failed to load page / Failed to wait until {} element was loaded @ "
                  "{}.".format(self.dom_id, self.url))
        finally:
            self.driver.quit()
