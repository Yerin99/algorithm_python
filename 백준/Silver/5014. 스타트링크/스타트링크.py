from collections import deque
from collections import defaultdict
from collections import defaultdict

f, s, g, u, d = map(int, input().split())
queue = deque([s])
depth = defaultdict(int)
visited = defaultdict(bool)
is_done = False

while queue:
    floor = queue.popleft()

    if floor == g:
        is_done = True
        break

    if not visited[floor]:
        if u != 0 and 1 <= floor + u <= f:
            queue.append(floor + u)
            depth[floor + u] = depth[floor] + 1

        if d != 0 and 1 <= floor - d <= f:
            queue.append(floor - d)
            depth[floor - d] = depth[floor] + 1

        visited[floor] = True


print(depth[g] if is_done else "use the stairs")