import re
def preprocess_query(query: str) -> dict:
    query = query.replace("El usuario busca ", "").strip()
    # Eliminar múltiples espacios intermedios
    query = re.sub(r'\s+', ' ', query)
    # Convertir a minúsculas da peores resultados
    # Eliminar caracteres especiales, mantener solo letras y números
    query = re.sub(r'[^\w\s]', '', query)
    # Eliminar stopwords da peores resultados
    return query