def factorial(n):
    """Bir sayının faktöriyelini hesaplar."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Faktöriyel negatif veya tam sayı olmayan bir değer için hesaplanamaz.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Bir sayının asal olup olmadığını kontrol eder."""
    if not isinstance(n, int) or n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """n terimli Fibonacci serisini döndürür."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Fibonacci serisi için pozitif bir tam sayı girin.")
    fib = [0, 1]
    if n <= 2:
        return fib[:n]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def gcd(a, b):
    """İki sayının en büyük ortak bölenini hesaplar."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """İki sayının en küçük ortak katını hesaplar."""
    return a * b // gcd(a, b)
