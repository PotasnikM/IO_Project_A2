import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time
import threading


temp ='''
{ 
        "list": [
            {
                "name": "ibum",
                "price": "10",
                "pizda": "10" 
            },
            {
                "name": "cerutin",
                "price": "10",
                "pizda": "10" 
            },
            {
                "name": "afsadfasdfsdfasdafasdf",
                "price": "10"  
            }
        ]
        "list1": [
            {
                "name": "ibum",
                "price": "10",
                "pizda": "10" 
            },
            {
                "name": "afsadfasdfsdfasdafasdf",
                "price": "10"  
            }
        ]
}
'''


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



    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--disable-popup-blocking")
    driver = uc.Chrome(options)



    driver.get(f"https://www.ceneo.pl/Zdrowie;szukaj-{res[0]}")
    temporary = res.copy()
    temporary.pop(0)
    print(temporary)
    for item in temporary:
        driver.execute_script(f"window.open('https://www.ceneo.pl/Zdrowie;szukaj-{item}')")

    all_tabs = driver.window_handles

    item_ind = 0

    results = {}

    for tab in all_tabs:

        driver.switch_to.window(tab)

        counter = 0
        #   IF THIS FAILS IT MEANS CAPTCHA BLOCKED THIS INSTANCE. IF THIS HAPPENS IT TRIES
        #   AGAIN INCREMENTIG COUNTER BY 1. IF COUNTER REACHES CERTAIN NUMBER THE PROGRAM GIVES UP
        while counter < 3:
            try:
                # driver.find_element(By.XPATH, "//*[@class='category-list-body js_category-list-body js_search-results js_products-list-main js_async-container']")
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                "//*[@class='category-list-body js_category-list-body js_search-results js_products-list-main js_async-container']")))
                break
            except:
                time.sleep(10)
                driver.refresh()

            counter += 1
        if counter == 3:
            print(f"Captcha error for product {res[item_ind]}, giving up")
            return "Captcha error"


            # THIS CHECKS WHETHER THIS PRODUCT IS AVALIABLE OR NOT
        elem = driver.find_element(By.XPATH,
                                   "//*[@class='category-list-body js_category-list-body js_search-results js_products-list-main js_async-container']/div[1]")

        if elem.get_attribute("class") == "alert":
            print(f"No such product as {res[item_ind]} available")
            continue

        #SCROLL TO THE BOTTOM TO LOAD IMAGES
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");

        path = "//*[@class='category-list-body js_category-list-body js_search-results js_products-list-main js_async-container']/div"
        num_of_suggestions = len(elem.find_elements(By.XPATH, path))

        if num_of_suggestions > 7:
            num_of_suggestions = 7

        # DICTIONARY OF THE SUGGESTED PRODUCTS GATHERED
        suggestions = [f"{res[item_ind]}"]

        for i in range(num_of_suggestions - 1):
            xpath = "//*[@class='category-list-body js_category-list-body " \
                    f"js_search-results js_products-list-main js_async-container']/div[{i + 1}]"

            # THE I-TH DIV IN TLE LIST OF PRODUCTS
            prod = elem.find_element(By.XPATH, xpath)

            # ACQUIRING NECESSARY ATTRIBUTES OF THE PRODUCT
            price = prod.get_attribute("data-productminprice")
            rating = prod.get_attribute("data-seorating")

            # SLIGHT CHANGE IN XPATH TO GET OTHER PARAMETERS
            xpath = f"// *[@class ='category-list-body js_category-list-body js_search-results " \
                    f"js_products-list-main js_async-container']/div[{i + 1}]/div[1]/div[1]/a"
            prod = elem.find_element(By.XPATH, xpath)

            link = prod.get_attribute("href")
            name = prod.get_attribute("title")

            xpath = f"// *[@class ='category-list-body js_category-list-body js_search-results " \
                    f"js_products-list-main js_async-container']/div[{i + 1}]/div[1]/div[1]/a/img"
            prod = elem.find_element(By.XPATH, xpath)
            img = prod.get_attribute("src")

            item = {"id": i}
            item["name"] = name
            item["price"] = price
            item["rating"] = rating[:-2]
            item["link"] = link
            item["img"] = img
            suggestions.append(item)
        results.append(suggestions)
        item_ind += 1

    json_fin = json.dumps(results, ensure_ascii=False, indent=2)
    print(json_fin)
    f = open("result.txt", "w")
    f.write(json_fin)
    f.close()










##########################################

    
if __name__=="__main__":
    start_scraper(temp)
     
    input()
        

    
    

    
    
    
    
    


          
