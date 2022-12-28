
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time
import random
import threading

temp ='''
{ 
        "list": [
            {
                "name": "dbiusdbciuasbduivcbusudiabdas",
                "price": "10"  
            },
            {
                "name": "ibum",
                "price": "12"
            },
            {
                "name": "biotebal",
                "price": "22" 
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
   
    for item in product_list:
        thread_instance = threading.Thread(target=scrape_product, args=(item,))
        thread_instance.start()
       

def scrape_product(product_name):
    options = Options()
    #options.add_argument("--headless")
    driver = uc.Chrome(options)
    
    driver.get(f"https://www.ceneo.pl/Zdrowie;szukaj-{product_name}")
    time.sleep(0.01)
    
    try:
        elem = driver.find_element(By.CLASS_NAME, 'category-list-body js_category-list-body js_search-results js_products-list-main js_async-container')
    except:
        print("No such product avaliable")
    
    
    
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
    
    
    
    
    


          
