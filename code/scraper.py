# Programa hecho por Valentin Sosa, vea mas de mis trabajos en:
# GitHub: https://github.com/fasiluva 
# Linkedin: https://www.linkedin.com/in/valentin-sosa-aa55a9294/.
# Todos los derechos de este codigo estan reservados!

from json import loads, dump  
from time import sleep  
from requests import Session  
from bs4 import BeautifulSoup  
import sys
import os
sys.path.append(os.path.abspath('..'))
from data.headers import request_data  
from data.categories import categories  

def scrap_all(limit: int = 50) -> None:
    """
    Scrapea todos los datos de la página, categoría por categoría.

    Este método recorre todas las categorías especificadas y las scrapea usando la función :func:`scrap_category`.

    Argumentos:
    - **limit** (*int*): El límite de productos a cargar por cada página. Valor por defecto: 50.
    
    Detalles de implementación:
    - Los *headers* requeridos para hacer la solicitud HTTP se obtienen de ``data/headers.py``.
    - El número máximo de páginas a cargar por categoría está limitado a 500.
    - Se utiliza una sesión persistente para manejar las cookies del sitio web y optimizar las peticiones HTTP.
    """

    headers = request_data
    session = Session()  
    
    for category in categories:
        scrap_category(category, session, headers, limit)
    
    session.close()
    return


def scrap_category(category: str, session: Session, headers: dict, limit: int, max_pages: int=500) -> None:
    """
    Scrapea la categoría pasada como argumento hasta agotar sus productos o hasta alcanzar la paginación `max_pages`.

    Argumentos:
    - category (str): La categoría a scrapear.
    - session (Session): Sesión HTTP persistente para hacer las solicitudes.
    - headers (dict): Headers HTTP necesarios para la solicitud.
    - limit (int): Límite de productos por página.
    - max_pages (int): Número máximo de páginas a scrapear (por defecto 500).

    Detalles de implementación:
    - La URL de cada página se construye en función de la categoría y el número de página.
    - Si una solicitud HTTP falla, se muestra un mensaje de error y se detiene el scraping de la categoría.
    - Los productos scrapeados se almacenan en `../data/raw_data/rd_{category}.json`.
    - Pausa de 2 segundos entre solicitudes para evitar sobrecargar el servidor.
    - Si la página no tiene contenido, el scraping termina.
    """

    all_products = []

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
            data = {}

            data_variants = loads(div_product_container['data-variants'])  
            data_variants = data_variants[0]
            
            link = div_product_container.select_one('a.item-link')
            title_product = link['title']
            url = link['href']
            
            data_variants["url"] = url
            data[title_product] = data_variants  
            
            all_products.insert(0, data)  

        print(f"\n\nPAGINA {page}\n\n")

        sleep(2) 

    with open(f'../data/raw_data/rd_{category}.json', 'w') as file:
        dump(all_products, file, indent=4) 

    return

# Para limit=70 tomo 2.3 minutos
# Para limit=12 (default) tomo 9.8 minutos 