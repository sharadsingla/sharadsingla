def fibonacci(n, fib = None):
    if fib is None:
        fib = [0, 1]

    if len(fib) >=n:
        return fib[0:n]
    else:
        result = fib[-2] + fib[-1]
        fib.append(result)

    return fibonacci(n, fib)



print(fibonacci(6))
