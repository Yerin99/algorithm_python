# input
a, b = map(int, input().split())

# solve
result = 1

while b > a:
    if b % 2 == 0:
        b //= 2
        result += 1
    elif b % 10 == 1:
        b //= 10
        result += 1
    else:
        break

if b != a:
    result = -1

# print
print(result)