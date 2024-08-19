# purposely added a bug
fib = []
def fibonacci(n):
    if n < 2:
        fib.append(n)
        return n
    else:
        result = fibonacci(n-2) + fibonacci(n-1)
        fib.append(result)
        return result 

print(fibonacci(6))
print(fib)
