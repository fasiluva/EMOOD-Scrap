# from pprint import pprint
import json
from time import sleep, perf_counter
import requests
from bs4 import BeautifulSoup
import sys
import os 
sys.path.append(os.path.abspath('..'))
from data.headers import request_data
from data.categories import categories


def scrap_all() -> None:
    """
    <h4> Scrapea todos los datos de la pagina, categoria por categoria. </h4> 
    
    * Usada en <code>code/refiner.py</code>
    """

    tiempoInicio = perf_counter()

    headers = request_data                  # Los headers estan en data/headers.py
    max_pages = 500                         # Maximo de paginas a cargar. Por defecto, 500.
    limit = 50

    session = requests.Session()            
    # Nos provee la cookie y una conexion persistente con la pagina 
    #! (obligatorio para moverse por paginaciones)
    
    for category in categories:
        scrap_category(category, session, max_pages, headers)
    
    session.close()
    print("\nTiempo tomado: ", perf_counter() - tiempoInicio)


def scrap_category(category : str, session : requests.Session, max_pages : int, headers : dict) -> None:
    """
    <h4> Scrapea la categoria pasada como argumento hasta agotar sus productos o hasta la paginacion <code>max_pages</code>.<h4>
    
    * Usada en <code>code/scraper.py</code>
    """

    all_products = []
    # Esta lista (tratada como una pila) sera escrita en el file al finalizar el scrapeo de la categoria.

    with open(f'../data/raw_data/rd_{category}.json', 'w') as file:
        print("\nCategoria: ", category)

        for page in range(1, max_pages):
            url = f"https://www.emoodmarket.com/{category}/page/{page}/?results_only=true&limit={limit}"
            response = session.get(url, headers=headers)

            if response.status_code != 200:
                print("\nERROR: Request denegada. Estado: ", response.status_code)
                s = input()
                return     

            soup = BeautifulSoup(response.text, 'html.parser')

            if soup.text == "":
                break

            for div_product_container in soup.select('div.js-product-container'):
                datos = {}
                data_variants = json.loads(div_product_container['data-variants'])
                data_variants = data_variants[0]
                link = div_product_container.select_one('a.item-link')
                title_product = link['title']
                url = link['href']
                
                data_variants["url"] = url
                datos[title_product] = data_variants
                all_products.insert(0, datos)           # Agregar el producto al inicio de la lista
                
                # print(title_product)
                # print(datos)

            print(f"\n\nPAGINA {page}\n\n")
            sleep(2)

        # Guardar todos los productos como un solo objeto JSON (lista de productos)
        json.dump(all_products, file, indent=4)

    return

scrap_all()

# Para limit=70 tomo 2.3 minutos
# Para limit=12 (default) tomo 9.8 minutos 