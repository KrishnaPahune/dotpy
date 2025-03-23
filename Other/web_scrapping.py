# Web scraping is the process of extracting data from websites automatically using a program or script.
# It involves fetching web pages and parsing their content to collect useful information. 

import requests
from bs4 import BeautifulSoup

url = "https://www.pravaraengg.org.in/"

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')

print(soup.prettify()) #this prints the code of the website

#This prints all the headings in the code
for heading in soup.find_all("h2"):
    print(heading.text)