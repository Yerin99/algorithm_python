from itertools import combinations

n = int(input())
s = list(map(int, input().split()))
is_exist = [False] * (sum(s) + 2)

for num in range(1, n+1):
    for e in combinations(s, num):
        is_exist[sum(e)] = True

for num in range(1, sum(s)+2):
    if not is_exist[num]:
        print(num)
        break
