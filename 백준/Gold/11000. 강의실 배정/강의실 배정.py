import sys, heapq
input = sys.stdin.readline

n = int(input())

arr = []
current = []

for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort()
heapq.heappush(current, arr[0][1])

for i in range(1, n):
    if(arr[i][0] < current[0]):
        heapq.heappush(current, arr[i][1])
    else:
        heapq.heappop(current)
        heapq.heappush(current, arr[i][1])

print(len(current))