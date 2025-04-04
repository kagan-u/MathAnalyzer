def clean_list(data):
    """Listeden None, boş string veya NaN gibi istenmeyen değerleri temizler."""
    return [x for x in data if x not in (None, "", float('nan')) and x is not False]

def sort_list(data, reverse=False):
    """Listeyi sıralar (varsayılan: artan)."""
    if not data:
        raise ValueError("Boş bir liste sıralanamaz.")
    return sorted(data, reverse=reverse)

def filter_list(data, condition):
    """Listeyi verilen koşula göre filtreler."""
    if not callable(condition):
        raise ValueError("Koşul bir fonksiyon olmalı.")
    return [x for x in data if condition(x)]

def group_list(data, key):
    """Listeyi verilen anahtar göre gruplar."""
    if not callable(key):
        raise ValueError("Anahtar bir fonksiyon olmalı.")
    result = {}
    for x in data:
        k = key(x)
        if k not in result:
            result[k] = []
        result[k].append(x)
    return result
