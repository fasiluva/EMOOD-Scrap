import json
from pprint import pprint
import sys
import os 
sys.path.append(os.path.abspath('..'))
from data.categories import categories

def refine_all():
    for category in categories: 
        refine_category(category)
        

def refine_category(category):
    listWrite = []

    with open(f"../data/raw_data/rd_{category}.json", "r") as fileRead:
    
        dict_products = json.load(fileRead)
    
        for dict_producto in dict_products:
            
            for producto_nombre in dict_producto:
                dictWrite = {
                    'nombre' : producto_nombre,
                    'sku' : dict_producto[producto_nombre]['sku'],
                    'precio' : dict_producto[producto_nombre]['compare_at_price_number'],
                    'precioDesc' : dict_producto[producto_nombre]['price_number'],
                    'metodosPago' : json.loads(dict_producto[producto_nombre]['installments_data']),
                    'categoria' : category,
                    'url' : dict_producto[producto_nombre]['url'],
                    'imagen' : dict_producto[producto_nombre]['image_url']
                }
                #pprint(dictWrite)
                listWrite.insert(0, dictWrite)
                
    with open(f"../data/clean_data/{category}.json", "w") as fileWrite: 
        json.dump(listWrite, fileWrite, indent=4)
    
refine_all()
"""
SKU 
Nombre
precio
precio c descuento
cuotas
categoría del producto
url
imagen
"""