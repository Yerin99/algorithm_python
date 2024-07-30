from itertools import combinations
from collections import defaultdict

n, s = map(int, input().split())
a = list(map(int, input().split()))
bound = int(n/2)
b, a = a[bound:], a[:bound]
a_length, b_length = len(a), len(b)
a_sum_dict, b_sum_dict = defaultdict(int), defaultdict(int)

answer = 0

for num in range(1, a_length+1):
    for e in combinations(a, num):
        a_sum_dict[sum(e)] += 1

for num in range(1, b_length+1):
    for e in combinations(b, num):
        b_sum_dict[sum(e)] += 1

for e in a_sum_dict.keys():
    answer += a_sum_dict[e] * b_sum_dict[s-e]
    if e == s:
        answer += a_sum_dict[e]

for e in b_sum_dict.keys():
    if e == s:
        answer += b_sum_dict[e]

print(answer)
