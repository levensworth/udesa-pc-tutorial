def fibo(n: int) -> int:
    if n in (0, 1):
        return 1
    return fibo(n-1) + fibo(n-2)

