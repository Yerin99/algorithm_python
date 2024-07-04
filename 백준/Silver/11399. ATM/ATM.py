n, p = int(input()), sorted(map(int, input().split()))
print(sum([p[i]*(n-i) for i in range(n)]))
