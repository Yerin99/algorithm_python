from collections import defaultdict


def dfs_backtracking(stack, start):
    if len(stack) == m:
        print(*stack)
        return 0

    for i in range(start, n+1):
        dfs_backtracking(stack + [i], i)
        

n, m = map(int, input().split())
count_dict = defaultdict(int)
dfs_backtracking([], 1)
