from core.loader import LoadPage
from core.scraper import ScrapePage
from core.compare import ComparePages

__author__='Pruthvi Kumar'
# 01 July 2019.
# pruthvikumar.123@gmail.com
# Extract, Scrape and Compare - Main entry-point.

# Step1 Load Page.
page = LoadPage('https://www.apricity.co.in', 'about')
page_source = page.extractor()

# Step2 Scrape page source into sink
ScrapePage()

# Step3 Compare and report differences between two pages.
ComparePages('./sink/apricity.txt', './sink/apricity.txt')
