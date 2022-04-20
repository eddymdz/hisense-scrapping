import requests
import json
import sys
from bs4 import BeautifulSoup as bs

# Note: when calling the script I pass arguments, the only arguments is for select the type of appliance (we should find what numbers correspond to each appliance?).

products_url = 'https://www.hisense-usa.com/support/modelOptions/' + sys.argv[1]
main_url = 'https://www.hisense-usa.com'
req = requests.get(products_url)
data = json.loads(req.text)
search_model = ""

print(sys.argv[1])

if (sys.argv[1] == "1"): # For TV's.
    search_model = "/tv-and-audio/televisions/all-tvs/"

elif (sys.argv[1] == "2"): # For refrigerators.
    search_model = "/home-appliance/refrigerators/all-refrigerators/"

elif (sys.argv[1] == "5"): # For audio devices.
    search_model = "/tv-and-audio/home-audio/"

for key, value in data['data'].items():
    model = key.split("/support/models/")
    product_details_url = main_url + search_model + model[1]
    print(value + ": " + product_details_url)
    req = requests.get(product_details_url)
    soup = bs(req.text, 'html.parser')
    
    # pdf_urls = soup.findAll("a", {"class":"ui-supportlinks__link"})
    specs = soup.find_all("div", {"class": "specifications-table"})

    for data in specs:
        data.select("th td")
        # title = a.select_one('.ui-supportlinks__title')
        
        print(data.getText())
        exit()
        
        # if(title.getText().find('Spec-Sheet') >= 0):
        #     print(a['href'])
        #     exit()
