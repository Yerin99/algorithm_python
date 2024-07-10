def fibonacci_dp(n):
    f[0], f[1], f[2] = 0, 1, 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


N = int(input())

f = [0]*(N+1)
answers = [fibonacci_dp(N), N-2]

print(*answers)
