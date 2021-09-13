def productOfDigits(n): return n if n < 10 else productOfDigits(n//10) * n % 10
