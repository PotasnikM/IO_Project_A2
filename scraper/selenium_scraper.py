import selenium
import json
from flask import Flask, request
from flask_cors import CORS
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



def start_scraper(json):
    x = 1
    
def search_product(product):
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

    
    
    
    
    
    


if __name__ == '__main__':
    options = Options()
    options.add_argument("--headless")
    driver = uc.Chrome(options=options)
    driver.get("https://google.pl/")
    element = driver.find_element(By.ID, "L2AGLb")
    driver.execute_script("arguments[0].click()", element)
    klub1 = input("Podaj pierwszą drużynę: ")
    klub2 = input("Podaj drugą drużynę: ")
    wyszukiwanie = klub1 + " " + klub2 + " ostatni mecz"
    element = driver.find_element(By.CSS_SELECTOR, 'input.gLFyf.gsfi')
    driver.execute_script("arguments[0].click()", element)
    wyszukiwarka = driver.find_element(By.NAME, "q")
    wyszukiwarka.clear()
    wyszukiwarka.send_keys(wyszukiwanie)
    wyszukiwarka.send_keys(Keys.ENTER)
    try:
        tablica_wyniku = driver.find_element(By.CSS_SELECTOR, 'div.imso_mh__ma-sc-cont')
    except selenium.common.exceptions.NoSuchElementException:
        tablica_wyniku = driver.find_element(By.CSS_SELECTOR, 'div.imso_mh__ma-sc-cont')
    elementy = tablica_wyniku.find_elements(By.CSS_SELECTOR, "*")
    wynik_spotkania = ""
    for temp in elementy:
        wynik_spotkania = wynik_spotkania + str(temp.get_attribute('innerHTML'))
    druzyny = str(driver.find_element(By.CSS_SELECTOR, 'div.IkSHxd.ellipsisize').get_attribute('innerHTML')).split(" ")
    data_spotkania = str(driver.find_element(By.XPATH, '//*[@id="sports-app"]/div/div[2]/div/div/div/div/div[1]/div[1]/div[1]/div/div/span[2]').get_attribute('innerHTML'))
    rozgrywki = str(driver.find_element(By.CLASS_NAME, "imso-ln").get_attribute('innerHTML'))
    print(rozgrywki + " " + data_spotkania + " ", end="")
    for e in druzyny:
        if str(e) != '–':
            print(e + " ", end="")
        else:
            print(wynik_spotkania + " ", end="")
          
