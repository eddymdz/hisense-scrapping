import requests
import json
from bs4 import BeautifulSoup as bs

products_url = 'https://www.hisense-usa.com/support/modelOptions/1'
main_url = 'https://www.hisense-usa.com'
r = requests.get(products_url)
data = json.loads(r.text)
for key,value in data['data'].items():
    product_details_url = main_url +  key
    print(value + ": " + product_details_url)
    r = requests.get(product_details_url)
    soup = bs(r.text,'html.parser')
    pdf_urls = soup.findAll("a", {"class":"ui-supportlinks__link"}) 
    for a in pdf_urls:
        title = a.select_one('.ui-supportlinks__title')
        if(title.getText().find('Spec-Sheet') >= 0):
            print(a['href'])
            exit()
