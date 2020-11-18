# Author: Parvathy Sudhakaran
# Purpose: This project does web scraping & parsing and thereby collects daily news from 2 sources - https://www.cbc.ca , https://globalnews.ca/
# Future Enhancement: Build a website to display the parsed news

from urllib.parse import urlparse

from bs4 import BeautifulSoup
from requests import get

def scraper():
    # *********************      CBC News scraping        ****************************
    soup_cbc = soupParse('https://www.cbc.ca')

    # from soup identify the class name corresponding to the area where all featured news are displayed
    featuredAreaSection = soup_cbc.find(class_='featuredArea')
    cbc_topstories_href = featuredAreaSection.find_all(class_='cardRegular')

    # find url of all news displayed in featured area section & save as a list
    newsHref = hrefParseList(cbc_topstories_href,'https://www.cbc.ca')
    print(newsHref)

    # *********************      GlobalNews scraping        ****************************
    soup_gn = soupParse('https://globalnews.ca/')

    # from soup identify the class name corresponding to the area where all featured news are displayed
    newsSection = soup_gn.find(class_='l-section__widget')
    focusedNews_link = newsSection.find_all(class_='c-posts__media')

    # find url of all news displayed in featured area section & save as a list
    storeisLink = hrefParseList(focusedNews_link,'https://globalnews.ca/')
    print(storeisLink)

def soupParse(url):
    # parse the html from website url
    html = get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    return soup

def hrefParseList(parsedHref, url):
    # this function retrieves the link of each news article
    href_list = [] # an empty list to store links of the all news article
    for i in range(len(parsedHref)):
        path = urlparse(parsedHref[i].get('href', None)).path
        href_list.append(url + path)  # this list contains links of all news to be displayed
    return href_list

# call the scraper function
scraper()