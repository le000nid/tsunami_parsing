import csv
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re

URL = "https://tidesandcurrents.noaa.gov/stations.html?type=Water+Levels"

driver = webdriver.Chrome()

driver.get(URL)
time.sleep(3)
soup = BeautifulSoup(driver.page_source, "lxml")
driver.close()

regions = [item['id'] for item in soup.find_all(class_='span12 areaheader')]

res = dict()

for reg in regions:
    reg_id = soup.find('div', {"class": "span12 areaheader", "id": reg})
    ids = [item.text for item in reg_id.find_all('div', {"class": re.compile("span4 station")})]
    res[reg] = ids

with open('coops_ids.csv', 'w') as f:
    fieldnames = ['region', 'ids', 'formatted_ids']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for key in res.keys():
        str_ids = []
        for s in res[key]:
            str_ids.append(s.split(' ')[0])
        writer.writerow({'region':key, 'ids':res[key], 'formatted_ids':str_ids})
