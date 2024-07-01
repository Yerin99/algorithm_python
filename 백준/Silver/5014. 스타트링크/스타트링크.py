from collections import deque
from collections import defaultdict

f, s, g, u, d = map(int, input().split())
queue = deque([s])

depth = defaultdict(lambda: -1)
depth[s] = 0

is_done = False

while queue:
    floor = queue.popleft()

    if floor == g:
        is_done = True
        break

    if u != 0 and 1 <= floor + u <= f and depth[floor + u] == -1:
        queue.append(floor + u)
        depth[floor + u] = depth[floor] + 1

    if d != 0 and 1 <= floor - d <= f and depth[floor - d] == -1:
        queue.append(floor - d)
        depth[floor - d] = depth[floor] + 1

print(depth[g] if is_done else "use the stairs")
