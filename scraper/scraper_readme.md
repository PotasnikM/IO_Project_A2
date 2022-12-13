#### SCRAPER REQUIERS THE FOLLOWING TO BE INSTALLED ####

selenium-webdriver version: 4.4.3 ---> # pip install selenium==4.4.3

Chrome version used: 108.0.5359.99

Chrome driver used: ChromeDriver 108.0.5359.71 --> https://chromedriver.storage.googleapis.com/index.html?path=108.0.5359.71/

#### FUNCTIONS DESCRIPTION ####
Function start_scraper() as input takes a json of products and parses it, acquiring only the names of the products
of interest. It then forwards them to function search_product() which opens a chrome webdriver instance and searches
for up to 10 most suitable products and returns their name, price. It is then forwarded to endpoint where user chooses their preferable option
 