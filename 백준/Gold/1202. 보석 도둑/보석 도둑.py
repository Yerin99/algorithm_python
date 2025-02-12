import heapq
import sys


input = sys.stdin.readline
n, k = map(int, input().split())
jewels, bags = [], []

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewels, (m, v))

for _ in range(k):
    c = int(input())
    heapq.heappush(bags, c)

result = 0
available_jewels = []

while bags:
    bag = heapq.heappop(bags)

    while jewels and jewels[0][0] <= bag:
        m, v = heapq.heappop(jewels)
        heapq.heappush(available_jewels, -v)

    if available_jewels:
        result += -heapq.heappop(available_jewels)

print(result)
