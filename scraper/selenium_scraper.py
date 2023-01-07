
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time
import random
import threading
import codecs

temp ='''
{ 
        "list": [
            {
                "name": "ibum",
                "price": "10",
                "pizda": "10" 
            },
            {
                "name": "ibum",
                "price": "10",
                "pizda": "10" 
            },
            {
                "name": "apap",
                "price": "10"  
            }  
        ]
}'''


# THIS FUNCTION PARSES JSON SENT BY THE USER AND INITIALIZES INSTANCE OF scrape_product()
# FOR EVERY PRODUCT NAME IN THE LIST   
def start_scraper(json_dict):
    
    try:
        products = json.loads(json_dict)
        product_list = []
        
        for section in products["list"]:
            product_list.append(section["name"])
    except:
        print("Invalid input format")
        return

    #REMOVE DUPLICATES
    res = []
    [res.append(x) for x in product_list if x not in res]

    for item in res:
        thread_instance = threading.Thread(target=scrape_product, args=(item, 0))
        thread_instance.start()
       

def scrape_product(product_name, counter):

    counter += 1
    options = Options()
    #options.add_argument("--headless")
    driver = uc.Chrome(options)
    
    driver.get(f"https://www.ceneo.pl/Zdrowie;szukaj-{product_name}")
    time.sleep(1)
    
    
    #   IF THIS FAILS IT MEANS CAPTCHA BLOCKED THIS INSTANCE. IF THIS HAPPENS IT TRIES
    #   AGAIN INCREMENTIG COUNTER BY 1. IF COUNTER REACHES CERTAIN NUMBER THE PROGRAM GIVES UP
    if counter < 3:
        try:
            #driver.find_element(By.XPATH, "//*[@class='category-list-body js_category-list-body js_search-results js_products-list-main js_async-container']")
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                    "//*[@class='category-list-body js_category-list-body js_search-results js_products-list-main js_async-container']")))
            
        except:
            print(f"Captcha error for product {product_name}, counter={counter}")
            driver.quit()
            time.sleep(15)
            scrape_product(product_name, counter)
            return
    else:
        print(f"Captcha error for product {product_name}, giving up")
        return    

    #THIS CHECKS WHETHER THIS PRODUCT IS AVALIABLE OR NOT
    elem = driver.find_element(By.XPATH,
                    "//*[@class='category-list-body js_category-list-body js_search-results js_products-list-main js_async-container']/div[1]")

    if elem.get_attribute("class") == "alert":
        print(f"No such product as {product_name} available")
        return

    num_of_suggestions = len(elem.find_elements(By.XPATH, './/div'))

    if num_of_suggestions > 6:
        num_of_suggestions = 6

    # DICTIONARY OF THE SUGGESTED PRODUCTS GATHERED
    suggestions = []

    for i in range(num_of_suggestions):

        xpath   = "//*[@class='category-list-body js_category-list-body " \
                f"js_search-results js_products-list-main js_async-container']/div[{i + 1}]"

        # THE I-TH DIV IN TLE LIST OF PRODUCTS
        prod    = elem.find_element(By.XPATH, xpath)

        # ACQUIRING NECESSARY ATTRIBUTES OF THE PRODUCT
        price   = prod.get_attribute("data-productminprice")
        rating  = prod.get_attribute("data-seorating")

        # SLIGHT CHANGE IN XPATH TO GET OTHER PARAMETERS
        xpath   = f"// *[@class ='category-list-body js_category-list-body js_search-results " \
                f"js_products-list-main js_async-container']/div[{i + 1}]/div[1]/div[1]/a"
        prod    = elem.find_element(By.XPATH, xpath)

        link    = prod.get_attribute("href")
        name    = prod.get_attribute("title")

        xpath   = f"// *[@class ='category-list-body js_category-list-body js_search-results " \
                f"js_products-list-main js_async-container']/div[{i + 1}]/div[1]/div[1]/a/img"
        prod    = elem.find_element(By.XPATH, xpath)
        img     = prod.get_attribute("src")

        item = {"id": i}
        item["name"]    = name
        item["price"]   = price
        item["rating"]  = rating[:-2]
        item["link"]    = link
        item["img"]     = img
        suggestions.append(item)


    json_fin = json.dumps(suggestions, ensure_ascii=False, indent=2)
    print(json_fin)
    f = open(f"{product_name}.txt", "w")
    f.write(json_fin)
    f.close()
    
if __name__=="__main__":
    start_scraper(temp)
     
    input()
        

    
    
""" def search_product(product):
    x = 1
    
# Define app and handle CORS errors
app = Flask(__name__)
CORS(app)
    
@app.route('/api/sendProd', methods=['POST'])
def start_scraper():
    data= json.loads(request.data)              # JSON sent from frontend
    color_thief = ColorThief(url['image'])      # Do sth with the data
    colors_arr = color_thief.get_palette(5, 1)
    response = {                                # Python dict with response
        "colors": []
    }

    for idx, each in enumerate(colors_arr):
    response["colors"].append({ "red": 0, "green": 0, "blue": 0 })
    response["colors"][idx]["red"] = each[0]
    response["colors"][idx]["green"] = each[1]
    response["colors"][idx]["blue"] = each[2]

    response = jsonify(response)               # Translate Python dict into JSON
    return response                            # Send response to frontend

app.run(host="localhost", port=5000)           # Run backend server on localhost:5000

     """
    
    
    
    
    


          
