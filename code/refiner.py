# Programa hecho por Valentin Sosa, vea mas de mis trabajos en:
# GitHub: https://github.com/fasiluva 
# Linkedin: https://www.linkedin.com/in/valentin-sosa-aa55a9294/.
# Todos los derechos de este codigo estan reservados!

from json import load, dump, loads  
import sys
import os
sys.path.append(os.path.abspath('..'))
from data.categories import categories  

def refine_all():
    """
    Refina todos los productos de las categorías definidas.
    """
    for category in categories: 
        refine_category(category)

    return 


def refine_category(category):
    """
    Refina los datos de productos de una categoría específica y los guarda en un archivo JSON limpio.

    Argumentos:
    - category (str): La categoría de productos a refinar.

    Detalles de implementacion: 
    - 
    """
    listWrite = []

    with open(f"../data/raw_data/rd_{category}.json", "r") as fileRead:
        dict_products = load(fileRead)  
    
        for dict_product in dict_products:
            for product_name in dict_product:
                dictWrite = {
                    'nombre': product_name,
                    'sku': dict_product[product_name]['sku'],
                    'precio': dict_product[product_name]['compare_at_price_number'],
                    'precioDesc': dict_product[product_name]['price_number'],
                    'metodosPago': loads(dict_product[product_name]['installments_data']), 
                    'categoria': category,
                    'url': dict_product[product_name]['url'],
                    'imagen': dict_product[product_name]['image_url']
                }
                listWrite.insert(0, dictWrite)

    with open(f"../data/clean_data/{category}.json", "w") as fileWrite: 
        dump(listWrite, fileWrite, indent=4)  

    return 
