import sys


def bf(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    # 전체 n - 1번의 라운드(round)를 반복
    for i in range(n):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(m):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1:
                    return True
    return False


input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
edges = []
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n + 1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])
