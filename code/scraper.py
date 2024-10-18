from pprint import pprint
import requests
from bs4 import BeautifulSoup
import sys
import os 
sys.path.append(os.path.abspath('..'))
from data.headers import request_data

def scrap():

    datos = {}

    categories = [
        "electrodomesticos", 
        "tecnologia", 
        "electronica-audio-video",
        "belleza-y-cuidado-personal",
        "muebles-y-sillas",              #? Hogar, muebles y jardin
        "herramientas",
        "bebes", 
        "instrumentos-musicales",
        "deportes-fitness",
        "alimentos-y-bebidas",
        "outlet",
        "ofertas"
        ]

    headers = request_data
    max_pages = 200

    for category in categories:
        url = f"https://www.emoodmarket.com/{category}/?mpage={max_pages}"

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print("\nERROR: Request denegada. Estado: ", response.status_code)
            s = input()
            return 

        soup = BeautifulSoup(response.text, 'lxml')

        soup = soup.select_one('div.js-product-table')
        
        # pprint(soup)
        
        for div_product_container in soup.select('div.js-product-container'):
            data_variants = div_product_container['data-variants']
            title_product = div_product_container.select_one('a.item-link')['title']

            print(title_product)
            print(data_variants)

            datos[title_product] = data_variants
            


        input()


scrap()

