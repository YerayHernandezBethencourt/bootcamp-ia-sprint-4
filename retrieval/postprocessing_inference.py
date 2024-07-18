"""
Función para procesar la respuesta del modelo.
Podríamos mostrar los datos de las 5 Top películas
"""

def postprocess_results(results: list) -> dict:
    """
    Postprocesa los resultados para devolverlos en el formato adecuado.
    
    Args:
    - results (list): Lista de películas recuperadas.
    
    Returns:
    - dict: Diccionario con los resultados formateados.
    """
    # Aquí va el código para postprocesar los resultados
    formatted_results = {"results": results}  # Ejemplo de salida
    return formatted_results