import sys
from itertools import combinations
import bisect

input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

# 눈덩이 높이 배열을 오름차순으로 정렬
heights.sort()

# 두 눈덩이의 합을 저장할 리스트
sums = []

# 모든 두 눈덩이의 합을 계산하여 리스트에 저장
for i in range(n):
    for j in range(i + 1, n):
        sums.append((heights[i] + heights[j], i, j))

# 두 눈덩이의 합 리스트를 정렬
sums.sort()

min_diff = float('inf')

# 두 눈덩이의 합 리스트에서 최소 차이를 찾기
for i in range(len(sums)):
    for j in range(i + 1, len(sums)):
        if sums[i][1] != sums[j][1] and sums[i][1] != sums[j][2] and sums[i][2] != sums[j][1] and sums[i][2] != sums[j][2]:
            min_diff = min(min_diff, abs(sums[i][0] - sums[j][0]))
            break  # 현재 i에 대해 j를 더 이상 볼 필요 없음

print(min_diff)