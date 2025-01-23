# input
n, m = map(int, input().split())

smart_people = list(map(int, input().split()))
s, smart_people = smart_people[0], smart_people[1:]

party_list = [[] for _ in range(m)]
ps = []

for i in range(m):
    party_people = list((map(int, input().split())))
    p, party_people = party_people[0], party_people[1:]
    party_list[i] = party_people
    ps.append(p)

# solve (dfs)
graph = [set() for _ in range(n+1)]

for i in range(m):
    p, party_people = ps[i], party_list[i]

    for j in range(p):
        for k in range(j+1, p):
            a, b = party_people[j], party_people[k]
            graph[a].add(b)
            graph[b].add(a)

stack = smart_people[:]
is_smart_people = [False]*(n+1)

while stack:
    node = stack.pop()
    if not is_smart_people[node]:
        is_smart_people[node] = True
        stack += list(graph[node])

result = 0

for party_people in party_list:
    is_fun_party = True

    for pp in party_people:
        if is_smart_people[pp]:
            is_fun_party = False
            break

    if is_fun_party:
        result += 1

print(result)
