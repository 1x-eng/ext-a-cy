from core.loader import LoadPage
from core.scraper import ScrapePage
from core.compare import ComparePages
from core.extractor import ExtractContents

__author__='Pruthvi Kumar'
# 01 July 2019.
# pruthvikumar.123@gmail.com
# Extract, Scrape and Compare - Main entry-point.

# Step1 Load Page.
page = LoadPage('https://www.apricity.co.in', 'about')
page_source = page.extractor()

# Step2 Scrape page source into si
scraper = ScrapePage(page_source, 'apricity')
scraper.extractor()

# Step3 Compare and report differences between two pages.
comparator = ComparePages('./sink/apricity.txt', './sink/ap2.txt', 'apricity_v_1')
comparator.compare()

# Step4 Extract respective DOM contents leveraging difference report.
extractor = ExtractContents('apricity_v_1', 'id')
extractor.extract_interested_dom_contents()
