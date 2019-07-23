from core.loader import LoadPage
from core.scraper import ScrapePage
from core.compare import ComparePages
from core.extractor import ExtractContents

__author__='Pruthvi Kumar'
# 01 July 2019.
# pruthvikumar.123@gmail.com
# Extract, Scrape and Compare - Main entry-point.

# Step1 Load Page.
page = LoadPage('https://angrygoldfish.aliexpress.com/store/feedback-score/1665279.html', 'shop121696428')
page_source = page.extractor()

# Step2 Scrape page source into si
scraper = ScrapePage(page_source, 'angrygoldfish')
scraper.extractor()  # This will extract contents of the whole page. Beware, iframe contents might not come through.
scraper.iframe_extractor('detail-displayer')  # This will scrape contents of inside an iframe with id - detail-displayer

# To check difference:
# 1. Scrape contents of the page conventionally. i.e. keep line 18 commented and execute until line 17.
# 2. Then rename sink file name in line 16, comment line 17 and uncomment line 18.
# 3. Execute until line 18.
# 4. Compare two sink files, the one with conventional scrape and another with iframe scrape.
# 5. In particular, search for 'we-wholesale-evaluation-detail' in conventional scrape, you will find nothing.
#    But, inside iframe scrape sink file, you will find `we-wholesale-evaluation-detail`. This confirms, that contents
#    inside an iframe can be scraped no problem.


# Step3 Compare and report differences between two pages.
# comparator = ComparePages('./sink/apricity.txt', './sink/ap2.txt', 'apricity_v_1')
# comparator.compare()
#
# # Step4 Extract respective DOM contents leveraging difference report.
# extractor = ExtractContents('apricity_v_1', 'class') # second parameter can be id/class
# extractor.extract_interested_dom_contents()
