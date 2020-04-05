'''''''''
Stock Market Scraping!
'''''''''


'''Variables'''
scrape_url = 'https://www.asx.com.au/asx/share-price-research/company/CBA'
save_location = r'C:/Users/wolfh/Desktop/Stock Market Scrapping Program/Logs/RawData/'  #need to make file frist

'''End Variables'''


'''Imports'''
from selenium import webdriver  # used to request info
# only needs part of bs4, renames BeautifulSoup to soup
from bs4 import BeautifulSoup as soup
from datetime import datetime
import time


'''Functions'''
def get_source():
    global scrape_url, scrape_html, driver
    driver = webdriver.Firefox()
    driver.get(scrape_url)
    scrape_html = driver.page_source
    driver.quit()
    return

def get_share_price():
    global scrape_html
    get_source()
    page_soup = soup(scrape_html, "html.parser")  # translate html website
    results = page_soup.find("div", {"class": "overview-section module overview-snapshot"})
    return(results.find("span").text)

def add_to_log(text):
    global save_location
    file = open(save_location, "a")
    file.write(str(text) + '% ')
    file.close()

def calculate_category():
    ###Work Needed###
    return

'''Set Variables'''
now = datetime.now()
final = []
yes = True
save_location = save_location + 'CBA_' + str(now.strftime("%d-%m-%Y")) + '.txt'


'''Main Code'''
while yes == True:
    now = datetime.now()
    if int(now.strftime("%H%M")) < 1600 and int(now.strftime("%H%M")) > 1000:
        try:
            share1
        except NameError:
            share1 = float(get_share_price())
        else:
            share2 = float(get_share_price())
            try:
                share1 = float(((share2 - share1) / share1)*100)
            except ZeroDivisionError:
                share1 = 0
            add_to_log(share1)
            share1 = share2
        time.sleep(600)
    else:
        print("Stock Market Closed, Current Time:", now.strftime("%H:%M"))
        time.sleep(60)
    
