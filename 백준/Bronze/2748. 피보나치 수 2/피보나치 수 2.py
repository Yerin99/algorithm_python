n = int(input())
fib = [0, 1]

for i in range(2, n+1):
    fib.append(fib[i-2] + fib[i-1])

print(fib[n])