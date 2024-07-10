import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer, bacon_num = 0, 1e90
bacon_results = [[-1]*(n+1) for i in range(n+1)]

for user in range(1, n+1):
    # 초기값 설정
    queue = deque([user])
    bacon_results[user][user] = 0

    while queue:
        person = queue.popleft()

        for friend in graph[person]:
            if bacon_results[user][friend] == -1:
                bacon_results[user][friend] = bacon_results[user][person] + 1
                queue.append(friend)

    bacon_result = sum(bacon_results[user][1:])

    if bacon_result < bacon_num:
        bacon_num = bacon_result
        answer = user

print(answer)
