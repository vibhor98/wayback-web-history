"""Script to crawl Wayback Machine's Summary page."""

import time
import requests
import lxml.html
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


data = pd.read_csv('Alexa-Top-sites.csv')

# Browser settings
options = webdriver.ChromeOptions()
options.add_argument('headless')
#browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# browser.set_page_load_timeout(15)

for i in range(71, len(data)):
    site = data.iloc[i]['Site'].lower()
    print(i, site)

    url = 'https://web.archive.org/details/' + site

    browser.get(url)
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.ID, 'container'))
        WebDriverWait(browser, timeout).until(element_present)
        inputElem = browser.find_elements(By.NAME, 'year_end')[1]
        print(inputElem.get_attribute('value'))
        inputElem.click()
        inputElem.clear()
        inputElem.send_keys('2005')
        # print(inputElem.get_attribute('value'))
    except TimeoutException:
        print("Timed out waiting for page to load")

    multiple_pages = True
    try:
        num_pages = len(browser.find_elements(By.CLASS_NAME, 'pagination-page'))
        pagination = browser.find_element(By.CLASS_NAME, 'pagination-back')
        # pagination = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pagination-back')))
    except:
        multiple_pages = False

    df = []
    for j in range(num_pages):
        html = browser.page_source
        tree = lxml.html.fromstring(html)
        res = tree.cssselect('div#react-wayback-search #WBDataSummary #container form div.table-wrapper div.form-group div.table_body table tbody tr')

        for tr in res[1:]:
            tds = tr.cssselect('td')
            df.append([tds[0].text_content(), tds[1].text_content().replace(',', ''),
                tds[2].text_content().replace(',', ''), tds[3].text_content().replace(',', '')])
        if multiple_pages:
            browser.execute_script("arguments[0].click();", pagination)
            # pagination.click()

    df = pd.DataFrame(df, columns=['type', 'captures', 'urls', 'new_urls']).to_csv(
                    './wayback_crawl_2005/' + site + '.csv', index=False)
