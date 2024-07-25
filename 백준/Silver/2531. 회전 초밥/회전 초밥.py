import sys

# input
input = sys.stdin.readline
n, kind_of_sushi, k, coupon_sushi = map(int, input().split())
sushi_list = [int(input()) for _ in range(n)]

# solve
coupon_sushi_exist = False

if coupon_sushi in sushi_list:
    coupon_sushi_exist = True

candidates = set()
start, end = 0, k

while start < n:
    if end <= n:
        eaten_sushi = sushi_list[start:end]
    else:
        eaten_sushi = sushi_list[start:] + sushi_list[:end % n]

    if coupon_sushi_exist:
        eaten_sushi.append(coupon_sushi)

    candidates.add(len(set(eaten_sushi)))
    start, end = start + 1, end + 1

answer = max(candidates)

if not coupon_sushi_exist:
    answer += 1

# print
print(answer)
