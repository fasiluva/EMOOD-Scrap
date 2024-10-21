# EMOOD-Scraper

Un programa hecho en Python que scrapea la tienda virtual [EMOOD](https://www.emoodmarket.com/). 

## Descripción

Este proyecto scrapea los datos de los productos de la página por categoría y los guarda en archivos `.json`. Consiste en 2 etapas: extracción y refinado. Se verán en detalle cada una de ellas en las siguientes secciones.

#### Requisitos

* `Python 3.0` o superior
* Librerías de Python: `requests`, `BeautifulSoup`, `json` y `time`
* Un navegador web, preferentemente uno de los siguientes: Google Chrome, Opera, Firefox (desconozco el funcionamiento del programa en otros navegadores).

#### Instalación

* Primero, instalamos `Python` (si no lo tenemos).
* Instalamos las librerías escribiendo en la terminal: `pip install requests && pip install BeautifulSoup4` (las demás normalmente vienen instaladas con Python).

### Layout del proyecto 

![Ubicación de los archivos en el directorio](https://github.com/fasiluva/EMOOD-Scrap/blob/main/assets/Layout.jpg)

* `scraper.py`: contiene las funciones de scrapeo de la página.
* `refiner.py`: contiene las funciones de refinado de los datos de la página.
* `utils.py`: vacio. Si necesitase de funciones auxiliares que no estén estrictamente relacionadas al archivo en donde se necesiten, irían aquí. (computar calculos numéricos o estadísticos, etc). 
* `categories.py`: contiene una lista con las categorías que tiene la página.
* `headers.py`: contiene un diccionario con los encabezados (headers) necesarios para hacer peticiones en la página.
* `/raw_data`: todo lo obtenido por la etapa de extracción es guardada en esta carpeta. Por cada categoría, hay un archivo `rd_categoria.json` que contiene los productos de dicha categoría.
* `/clean_data`: todo lo obtenido por la etapa de refinado es guardado en esta carpeta. Por cada categoría, hay un archivo `categoria.json` que contiene los datos relevantes de los productos de dicha categoría.
* `test.py`: contiene funciones para testeo de `scraper.py` y `refiner.py`
* `/assets`: imágenes usadas para la documentación. 

#### Etapa de extracción de datos: 

La etapa de extracción se encarga de hacer todas las peticiones necesarias a la página y guardar los datos en un archivo `.json`. El archivo encargado de hacer esto es `scraper.py`, que a su vez hace uso de `categories.py` y `headers.py`. Dentro de `scraper.py`, tenemos las funciones:

* `scrap_category`, que scrapea en la página de EMOOD los productos de una categoría pasada como argumento (ver los demás parámetros en su definición).
* `scrap_all`, que, haciendo uso de la función anterior, scrapea todas las categorías.

#### Etapa de refinado de datos:

La etapa de refinado se encarga de revisar los datos de los productos obtenidos en la etapa anterior, conservando solo aquellos que son relevantes para cada producto. El archivo encargado de hacer esto es `refiner.py`, que a su vez hace uso de `categories.py`. Dentro de `refiner.py`, tenemos las funciones: 

* `refine_category`, que refina todos los datos del archivo `.json` correspondiente a la categoría pasada como argumento y los guarda en un nuevo `.json`.
* `refine_all`, que, haciendo uso de la función anterior, refina todas las categorías.

### Ejecución

Para testear las funciones, recomiendo que haga uso del archivo `test.py` ubicado en la carpeta `tests`, ya que el mismo tiene los archivos de ambas etapas importados y ha sido acomodado para que pueda cronometrar el rendimiento de las funciones. Puede importar el archivo `test.py` desde donde usted quiera.

## Autores

Hecho por Valentín Sosa. Vea más de mis trabajos en: <br>
GitHub: https://github.com/fasiluva <br>
LinkedIn: https://www.linkedin.com/in/valentin-sosa-aa55a9294/.

## Licencia

Este proyecto está protegido por derechos de autor y todos los derechos están reservados. Lea el archivo `LICENSE`.
