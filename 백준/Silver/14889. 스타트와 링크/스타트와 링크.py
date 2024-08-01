import sys

# input
input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]


def dfs(depth, people):  # solve
    global n, min_diff
    if depth == depth_limit:
        half_s = another_s = 0

        others = list(set(range(1, n+1)) - set(people))

        for i in range(len(people)):
            for j in range(i+1, len(people)):
                p1, p2 = people[i]-1, people[j]-1
                half_s += s[p1][p2]
                half_s += s[p2][p1]

        for i in range(len(others)):
            for j in range(i+1, len(others)):
                o1, o2 = others[i]-1, others[j]-1
                another_s += s[o1][o2]
                another_s += s[o2][o1]

        diff = abs(another_s - half_s)
        min_diff = min(diff, min_diff)
        return 0

    for i in range(1, n+1):
        if not people or people[-1] < i:
            people.append(i)
            dfs(depth+1, people)
            people.pop()


min_diff = 1e90
depth_limit = n // 2
visited = [False]*(n+1)
dfs(0, [])

# print
print(min_diff)
