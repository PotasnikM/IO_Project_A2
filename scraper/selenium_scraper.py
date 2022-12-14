
import json

temp ='''
{ 
        "list": [
            {
                "name": "Apap",
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
        print("invalid input format")
        
    for item in product_list:
        scrape_product(item)

def scrape_product(product_name):
    print()
    
   
    
    
    
if __name__=="__main__":
    start_scraper(temp)    
        

    
    
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
    
    
    
    
    


          
