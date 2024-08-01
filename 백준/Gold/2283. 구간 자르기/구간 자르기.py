import sys

LIMIT = 1000000
input = sys.stdin.readline
n, k = map(int, input().split())

# 이모스 알고리즘을 위한 배열
imos = [0] * (LIMIT + 2)

# 구간 정보 입력
for _ in range(n):
    a, b = map(int, input().split())
    imos[a] += 1
    imos[b] -= 1

# 이모스 알고리즘을 적용하여 누적합 계산
for i in range(1, LIMIT + 2):
    imos[i] += imos[i - 1]

# 투 포인터 알고리즘을 사용하여 구간 찾기
left = right = 0
length = 0
result = (0, 0)

while right <= LIMIT:
    if length < k:
        right += 1
        length += imos[right - 1]
    elif length > k:
        length -= imos[left]
        left += 1
    else:  # length == k
        result = (left, right)
        break

    if left > right:
        right = left

# 결과 출력
if result == (0, 0):
    print("0 0")
else:
    print(result[0], result[1])