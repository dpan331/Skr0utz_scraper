"""
created by Dimitrios Panourgias
May 2020

Not to be used for commercial or any other purpose
that might harm the smooth operation of Skroutz.gr
"""




from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def getProductList():
    """
    Feed the script with a product list (in csv format, no headers)
    that you desire to investigate via Skroutz.gr
    If the Skroutz search bar provides a product, fetch the data directly,
    else pick the best match between the search results and the search query
    """
    productCSV = pd.read_csv('../skroutz/productList.csv', header=None)
    productList = productCSV.values.tolist()
    # initiate the dataframe that will collect all data
    dataTable = pd.DataFrame(columns=['product_name', 'label', 'shop_name', 'initial_price',
                                      'ship_cost', 'pay_cost', 'final_price', 'availability'])
     
    #### HIDDEN CODE ROWS ###
        
    return endResult


def bestLinkMatch(seedLink, pageLinks):
    """
    Perform word count frequency between our desired product
    and the results of skroutz search bar.
    Return the best match.
    NEEDS OPTING!!!!!!
    """
    seedLink = seedLink.split()
    numMatch = []
    bestLink = pageLinks[0]
    for i in range(0, len(pageLinks)):
     
    #### HIDDEN CODE ROWS ###
        
    return bestLink


def fetchDataForProduct(productURL, productName, labl, df):
    """
    Fetches the data (shop name, initial price, shipping cost, pay-to-delivery cost, final price)
    of a specific product
    """
    driver = webdriver.Chrome('C:/Users/dimpa/Downloads/chromedriver.exe')
    driver.get(productURL)
    driver.maximize_window()
    time.sleep(10)
    SCROLL_PAUSE_TIME = 5

    ### HIDDEN CODE ROWS ###
    
    driver.quit()
    return df


finalDf = getProductList()
finalDf.to_csv('resultsList.csv')
