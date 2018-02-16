#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time

url = "https://www.recreation.gov/campsiteCalendar.do?page=calendar&contractCode=NRSO&parkId=70928&calarvdate=07/12/2018&sitepage=true&startIdx=0"
page = requests.get(url, verify=False)
soup = BeautifulSoup(page.content, "html.parser")
data = []
table = soup.find("table", attrs={"name": "calendar", "id": "calendar"})
table_body = table.find("tbody")
rows = table_body.find_all("tr")
for row in rows:
  cols = row.find_all("td")
  cols = [ele.text.strip() for ele in cols]
  # only cache the cols that are not weird
  if len(cols) > 1:
    data.append(cols)

for row in data:
  site = row[0].split("\n\n")[1]
  th = row[2]
  fr = row[3]
  sa = row[4]
  if site in ["030", "031", "032", "033"]:
    print "site: {}, thursday={}, friday={}, saturday={}".format(site, th, fr, sa)

print url
