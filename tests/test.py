# Programa hecho por Valentin Sosa, vea mas de mis trabajos en:
# GitHub: https://github.com/fasiluva 
# Linkedin: https://www.linkedin.com/in/valentin-sosa-aa55a9294/.
# Todos los derechos de este codigo estan reservados!

import sys
from time import perf_counter
import os
sys.path.append(os.path.abspath('../code'))

import scraper
import refiner


def test_scraper(limit : int) -> int:
    """
    Funcion usada para testear las demas definidas.    
    """

    inicio = perf_counter()
    scraper.scrap_all(limit)
    total = perf_counter() - inicio

    print(f"Tiempo tomado para scraper.py con limit={limit}: {total}")
    
    return total


def test_refiner() -> int: 

    inicio = perf_counter()
    refiner.refine_all()
    total = perf_counter() - inicio

    print("Tiempo tomado para refiner.py: ", total)

    return total


def test(limit : int = 50) -> int:
    """
    Funcion usada para testear las demas definidas.    
    """

    inicio = test_scraper(limit)
    total = test_refiner() + inicio
    
    print("Tiempo total tomado para ambas funciones: ", total)

    return total


"""
Tiempo tomado para scraper.py con limit=50:  168.45443549996708
Tiempo tomado para refiner.py:  0.6162515999749303
Tiempo total tomado para ambas funciones:  169.070687099942

168 segundos = 2:48 minutos
"""