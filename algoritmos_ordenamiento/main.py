import random
import time

def generar_arreglo(tamanio):
    return [random.randint(1, 1000) for _ in range(tamanio)]

def imprimir_arreglo(arreglo):
    print(arreglo)

def busqueda_secuencial(arreglo, elemento):
    for i, num in enumerate(arreglo):
        if num == elemento:
            return i
    return -1

def ordenar_arreglo(arreglo):
    return sorted(arreglo)


if __name__ == "__main__":
    tamanio_arreglo = 1000
    
    # Paso 1: Generar arreglo
    inicio = time.time()
    arreglo = generar_arreglo(tamanio_arreglo)
    fin = time.time()
    print(f"""Arreglo generado en {fin - inicio}, segundos
          
          """)

    # Paso 2: Imprimir arreglo
    imprimir_arreglo(arreglo)

    # Paso 3: Búsqueda secuencial
    elemento_buscado = arreglo[random.randint(0, tamanio_arreglo - 1)]
    inicio = time.time()
    indice = busqueda_secuencial(arreglo, elemento_buscado)
    fin = time.time()
    if indice != -1:
        print(f"""
            
        Elemento {elemento_buscado} encontrado en el índice {indice}.
            """)
    else:
        print(f"Elemento {elemento_buscado} no encontrado.")
    print(f"""

        Búsqueda secuencial realizada en, {fin - inicio}, segundos
        """)

    # Paso 4: Ordenar arreglo
    inicio = time.time()
    arreglo_ordenado = ordenar_arreglo(arreglo)
    fin = time.time()
    print("""
        
        Arreglo ordenado en", fin - inicio, "segundos""")

    # Paso 5: Búsqueda secuencial en arreglo ordenado
    inicio = time.time()
    indice = busqueda_secuencial(arreglo_ordenado, elemento_buscado)
    fin = time.time()
    if indice != -1:
        print(f"""

        Elemento {elemento_buscado} encontrado en el índice {indice}.""")
    else:
        print(f"""

        Elemento {elemento_buscado} no encontrado.""")
    print("""
        Búsqueda secuencial en arreglo ordenado realizada en", fin - inicio, "segundos""")
    
