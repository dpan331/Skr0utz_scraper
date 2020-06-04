# Skr0utz_scraper
Python script (back-end) created by Dimitrios Panourgias
<br/> Google sheet (front-end) created by Dimitrios Panourgias
<br/> May 2020

This script **does not by any means aim
to cause any harm to the website
that uses to scrap data.** <br/> For this purpose, the
requests that are set by the script are performed
relatively slow, simulating the speed of a human user.

It can retrieve numerous product details and along with the Google Sheet model provide comparative price analysis with up to 3 competitors of the user's choice.

## Python script (back-end) 
The script reads a csv (productList.csv) with product names (manual input). 
<img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/productsList.JPG" height="150" width="600">

<br/> Then proceeds to search each product name (from the csv) in Skroutz's search bar. 
<img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/productSearchBar.JPG" height="150" width="600">

<br/> If the result is a single product, the script proceeds to this product page (and applies the label: "original"),
<br/> otherwise -if the search matches multiple products- the script retrieves the results' product names, performs word matching to pick the best match with the desired product and then proceedσ to the product page.
<img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/bestMatch.JPG" height="400" width="500">

<br/> Once in the product page, the script iterates over all the shops using Selenium, retrieves for each shop the fields: initial price, shipping cost, pay-to-delivery cost, final price & availability, and pushes these information to a dataframe.
<img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/fetchData.JPG" height="400" width="600">

<br/> Finally, the aggregated data in the dataframe are exported in a csv (resultsList.csv).
<br/> 

## Google sheet (front-end)
For better comprehension and visualization of the retrieved information, the data from resultsList.csv can be passed to the Google Spreadsheet's sheet "raw".

<br/> By following the instructions, the data are processed and provided elegantly in the "analysis" sheet. Specifically, the user defines his/her shop name and & to 3 competitors, and the model provides a competitive price analysis.

<br/> <img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/googleSheetSkroutz.JPG" height="200" width="6800">



### Other actions
<br/> *- The visualization can be set to any tool you prefer, Excel, Google Data Studio, Power BI, Tableau, etc.*
<br/> *- The front-end analysis can be expanded depending on additional data the shop owner can provide. Imagine having the profit margin (shop's average, product categories' or even granular to each product) and also matching Skroutz's commission (according to the shop owner's chosen cost model). The possibilities for further analysis are endless!*
<br/> *- The python script is not complete. Minor fixes can further improve the performance (i.e. in the situation where Skroutz's search bar provides as a result a single product that is provided by a sole seller, the route is redirected to the seller's website. The python script could specify this to the dataframe and not omit this product.)*

