n = int(input())
meetings = []

for _ in range(n):
    s, e = map(int, input().split())
    meetings.append([s, e])

meetings.sort(key=lambda x: (x[1], x[0]))

answer = 0
last_end = 0

for s, e in meetings:
    if s >= last_end:
        last_end = e
        answer += 1

print(answer)
