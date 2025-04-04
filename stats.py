# MathAnalyzer/stats.py
from collections import Counter

def mean(data):
    """Veri listesinin ortalamasını hesaplar."""
    if not data or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Geçerli bir sayı listesi girin.")
    return sum(data) / len(data)

def median(data):
    """Veri listesinin medyanını hesaplar."""
    if not data or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Geçerli bir sayı listesi girin.")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]

def mode(data):
    """Veri listesinin modunu (en sık tekrar eden değeri) hesaplar."""
    if not data:
        raise ValueError("Boş bir liste için mod hesaplanamaz.")
    counter = Counter(data)
    max_count = max(counter.values())
    return [k for k, v in counter.items() if v == max_count]

def variance(data):
    """Veri listesinin varyansını hesaplar."""
    if not data or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Geçerli bir sayı listesi girin.")
    avg = mean(data)
    return sum((x - avg) ** 2 for x in data) / len(data)
