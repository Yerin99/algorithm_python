import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

for i in range(m):
    new = 0

    for j in range(2):
        new += heapq.heappop(cards)

    for j in range(2):
        heapq.heappush(cards, new)

print(sum(cards))
