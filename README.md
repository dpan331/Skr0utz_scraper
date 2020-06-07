# Skr0utz_scraper
Python script (back-end) created by **Dimitrios Panourgias**
<br/> Google sheet (front-end) created by **Dimitrios Panourgias**
<br/> May 2020

This script **does not by any means aim
to cause any harm to the website
that uses to scrap data.** <br/> The
requests that are set by the script are performed
relatively slow, simulating the speed of a human user.
<br/> Still, this script is **only for personal portfolio & educational purposes** and not destined to be used by third parties for commercial or any other purpose that might harm the smooth operation of the source website.
<br/> **Keep in mind that, according to Skr0utz.gr terms, navigating the website with the use of automated software is prohibited.**

:children_crossing: *This script is not maintained, so, in time, certain operations or even the entire script may not be functional.* 

<br/> **Scope of the script:**
<br/> The script can retrieve numerous product details and along with the Google Sheet model provide comparative price analysis with up to 3 competitors of the user's choice.

## Python script (back-end) 
The script reads a csv (productList.csv) with product names (manual input). 
<img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/productsList.JPG" height="150" width="600">

<br/> Then proceeds to search each product name (from the csv) in Skr0utz's search bar. 
<img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/productSearchBar.JPG" height="150" width="600">

<br/> If the result is a single product, the script proceeds to this product page (and applies the label: **"original"**),
<br/> otherwise -if the search matches multiple products- the script retrieves the results' product names, performs word matching to pick the best match with the desired product (applies the label: **"best_match"**) and then proceeds to the product page.
<img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/bestMatch.JPG" height="400" width="500">

<br/> Once in the product page, the script iterates over all the shops (using Selenium), retrieves for each shop the fields: **initial price, shipping cost, pay-to-delivery cost, final price & availability**, and pushes these information to a dataframe.
<img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/fetchData.JPG" height="400" width="600">

<br/> Finally, the aggregated data in the dataframe are exported in a csv (resultsList.csv).
<br/> 

## Google sheet (front-end)
For better comprehension and visualization of the retrieved information, the data from resultsList.csv can be passed to the Google Spreadsheet's sheet "raw". *Here you can find the [Google Sheet link](https://docs.google.com/spreadsheets/d/1g7CexOitbikx4CX66RlHmEX_53-S-RsEajCs8srZftU/edit?usp=sharing). Here you will find the downloaded version (in .xlsx format) of the Google Spreadsheet. Thus certain formulas in some cells do not operate.*

<br/> By following the "instructions" sheet, the data are processed and provided elegantly in the "analysis" sheet. Specifically, **the user defines his/her shop name and & to 3 competitors, and the model provides a comparative price analysis.**

<br/> <img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/googleSheetSkroutz.JPG" height="200" width="6800">



## Further actions
*- The visualization can be set to any tool you prefer: Excel, Google Data Studio, Power BI, Tableau, etc.*
<br/> *- The front-end analysis can be expanded depending on additional data the shop owner can provide. Imagine having the profit margin (shop's average, product categories' or even granular to each product) and also matching Skr0utz's commission (according to the shop owner's chosen cost model). The possibilities for further analysis are endless!*
<br/> *- The python script is not complete. Minor fixes can further improve the performance (i.e. in the situation where Skroutz's search bar provides as a result a single product that is provided by a sole seller, the route is redirected to the seller's website. The python script could specify this to the dataframe and not omit this product).*


<br/> <img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/it-crowd-moss-fire.jpg" height="200" width="350">

