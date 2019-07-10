from selenium import webdriver
import csv
import os

__author__ = 'Pruthvi Kumar'


# 10 July 2019.
# pruthvikumar.123@gmail.com
# Extract key element attributes of an identified sraped webpage.


class ExtractContents:

    def __init__(self, file_name, extraction_type):
        super(ExtractContents, self).__init__()
        self.file_name = file_name
        self.extraction_type = extraction_type
        self.driver = webdriver.Chrome()

    def extract_interested_dom_contents(self):
        try:
            self.driver.get('file://{}/../difference_report/{}_changed_contents.html'.format(os.path.dirname(__file__),
                                                                                             self.file_name))
        except Exception as e:
            print('Unable to mount given file in {} to webdriver. Stack trace to follow'.format(self.file_name))
            print(str(e))

        try:
            # create extraction_report folder if not exists.
            os.makedirs('{}/../extraction_report'.format(os.path.dirname(__file__)), exist_ok=True)

            with open('{}/../extraction_report/{}.csv'.format(os.path.dirname(__file__), self.file_name), 'w') as erf:
                writer = csv.writer(erf)
                elements = self.driver.find_elements_by_xpath('//*[@{}]'.format(self.extraction_type))
                writer.writerow(['REFERENCE FROM: {}_changed_contents.html from within difference_report '
                                 'folder.'.format(self.file_name)])

                writer.writerow(['TAG NAME', 'DOM ELEMENT - {}'.format(self.extraction_type)])
                for element in elements:
                    writer.writerow([element.tag_name, element.get_attribute(self.extraction_type)])

                writer.writerow(
                    ['PS: ACTION POINT FROM THIS REPORT IS -  ALL ELEMENTS LISTED ABOVE ARE DOM ELEMENTS THAT '
                     'HAVE CHANGED BETWEEN TWO VERSIONS OF SOFTWARE THAT WAS PROVIDED TO COMPARATOR PIPELINE STEP.'])

        except Exception as e:
            print('Unable to extract elements with {} attributes from given source @ {}. '
                  'Stack trace to follow'.format(self.extraction_type, self.file_name))
            print(str(e))

        finally:
            self.driver.quit()
