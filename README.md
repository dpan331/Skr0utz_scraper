# Skr0utz_scraper
Python script (back-end) created by Dimitrios Panourgias
<br/> Google sheet (front-end) created by Dimitrios Panourgias
<br/> May 2020

This script **does not by any means aim
to cause any harm to the website
that uses to scrap data.** <br/> For this purpose, the
requests that are set by the script are performed
very slowly, simulating the speed of a human user.


## Python script (back-end) 
The script reads a csv (productList.csv) with product names (manual input). 

Then proceeds to search each product name (from the csv) in Skroutz's search bar. 
<br/> If the result is a single product, the script proceeds to this product page (and applies the label: "original"),
<br/> otherwise -if the search matches multiple products- the script retrieves the results' product names, performs word matching to pick the best match with the desired product and then proceedσ to the product page.

Once in the product page, the script iterates over all the shops using Selenium, retrieves for each shop the fields: initial price, shipping cost, pay-to-delivery cost, final price & availability, and pushes these information to a dataframe.

Finally, the aggregated data in the dataframe are exported in a csv (resultsList.csv).


## Google sheet (front-end)
For better comprehension and visualization of the retrieved information, the data from resultsList.csv can be passed to the Google Spreadsheet's sheet "raw".

By following the instructions, the data are processed and provided elegantly in the "analysis" sheet. Specifically, the user defines his/her shop name and & to 3 competitors, and the model provides a competitive price analysis.
