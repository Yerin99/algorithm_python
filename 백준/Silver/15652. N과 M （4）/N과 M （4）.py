from collections import defaultdict


def dfs_backtracking(start):
    if len(stack) == m:
        print(*stack)

    for i in range(start, n+1):
        if count_dict[i] < m:
            count_dict[i] += 1
            stack.append(i)
            dfs_backtracking(i)
            stack.pop()
            count_dict[i] -= 1


n, m = map(int, input().split())
stack = []
count_dict = defaultdict(int)
dfs_backtracking(1)
