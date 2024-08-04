def dfs_backtracking(stack):
    if len(stack) == m:
        print(*stack)
        return 0

    for num in nums:
        dfs_backtracking(stack + [num])


n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))
dfs_backtracking([])
