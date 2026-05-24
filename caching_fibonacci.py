
def caching_fibonacci():
    cache = {}
    def fibonacci(n: int):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
            return result

    return fibonacci

fib = caching_fibonacci()
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(10))
print(fib(15))
