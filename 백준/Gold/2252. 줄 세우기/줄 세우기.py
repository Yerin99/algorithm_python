import sys
from collections import deque

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())

    from typing import List

    graph: List[List[int]] = [[] for _ in range(n + 1)]
    in_degree = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1

    queue = deque()

    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)

    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for next_node in graph[current]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)

    print(*result)


if __name__ == "__main__":
    main()
