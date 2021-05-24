from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

"""

This algorithm does not by any means aim
to cause any harm to the online source
that uses to scrap data. For this purpose, the
requests that are set by the algorithm are performed
very slowly, simulating the speed of a human user.

"""

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
    # declare iterator to concat dataframes
    it = 0
    for product in productList:
        strProd = ""
        strProd = strProd.join(product)
        urlSearch = 'https://www.skroutz.gr/search?keyphrase=' + strProd
        searchProduct = simple_get(urlSearch)
        html = BeautifulSoup(searchProduct, 'html.parser')
        # Fetch the itemtype of the search result page (Product or WebPage)
        htmlItemType = html.find('html').attrs
        splitHtmlItemType = htmlItemType['itemtype'].split('/')
        # if itemtype == Product then label = original
        # if itemtype == WebPage then label = bestmatch
        label = 'original'
        if 'Product' in splitHtmlItemType: # meaning single product search result, itemtype == Product
            if it == 0: # for the first iteration feed the fetchDataForProduct function the initial empty dataframe
                endResult = fetchDataForProduct(urlSearch, strProd, label, dataTable)
                it += 1
            else: # for the next iterations refeed the fetchDataForProduct function with the populated dataframe
                endResult = fetchDataForProduct(urlSearch, strProd, label, endResult)
                it += 1
        else: # meaning multiple search bar results, itemtype == WebPage
            label = 'best_match'
            # get the link of each search bar result
            anchors = html.find_all('a', {'class': 'js-sku-link', 'href': True})
            anchor_list = []
            for anchor in anchors:
                anchor_list.append(anchor['href'])
            # call the bestLinkMatch function to identify the search bar result that
            # best matches the search query product
            bestProductMatch = 'https://www.skroutz.gr' + bestLinkMatch(urlSearch, anchor_list)
            if it == 0: # for the first iteration feed the fetchDataForProduct function the initial empty dataframe
                endResult = fetchDataForProduct(bestProductMatch, strProd, label, dataTable)
                it += 1
            else: # for the next iterations refeed the fetchDataForProduct function with the populated dataframe
                endResult = fetchDataForProduct(bestProductMatch, strProd, label, endResult)
                it += 1
        time.sleep(10)
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
        y = pageLinks[i].split("-")
        results = {}
        for g in seedLink:
            results[g] = y.count(g)
        numMatch.append(sum(results.values()))
        # split seedlink and pagelinks to words and count the identical words between them
        # if count of identical words matches and len of words is same or less declare best match
        if (numMatch[i] == len(seedLink) and len(seedLink) >= len(y)):
            bestLink = pageLinks[i]
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
    # Get scroll height till bottom of page
    last_height = driver.execute_script("return document.body.scrollHeight")
    # Define scroll iterator
    scr_down = 600
    while True: # scroll down the page step by step to simultaneously fetch the data
        x = 'window.scrollTo(0, ' + str(scr_down) + ')'
        driver.execute_script(x)
        scr_down += 600 # define the step to scroll down
        time.sleep(SCROLL_PAUSE_TIME)
        if (scr_down == last_height or scr_down > last_height): # define the break condition for the loop
            break
        shopName = driver.find_elements(By.CLASS_NAME, 'shop-name')
        priceContent = driver.find_elements(By.CLASS_NAME, 'price-content')
        availability = driver.find_elements(By.CLASS_NAME, 'availability')
    # declare the dataframe that populates the data for the specific product
    df_add = pd.DataFrame(columns=['product_name', 'label', 'shop_name', 'initial_price',
                                   'ship_cost', 'pay_cost', 'final_price', 'availability'])
    # fetch data for each shop name that appears in the product results
    for i in range(0, len(shopName)):
        x = shopName[i].text
        y = priceContent[i].text
        z = availability[i].text
        y_cl = y.split()
        try:
            # the product name is needed to appear duplicated in each row
            # to ease the use of pivot tables later
            # the same holds for the label
            df_add = df_add.append({'product_name': productName,
                                    'label': labl,
                                    'shop_name': x,
                                    'initial_price': y_cl[0],
                                    'ship_cost': y_cl[3],
                                    'pay_cost': y_cl[7],
                                    'final_price': y_cl[10],
                                    'availability' : z},
                                    ignore_index=True)
        except:
            continue
    df = pd.concat([df, df_add], axis=0, ignore_index=True)
    print(df_add)
    driver.quit()
    return df


finalDf = getProductList()
finalDf.to_csv('resultsList.csv')
