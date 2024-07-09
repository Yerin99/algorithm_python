import sys

# input
lines = []

for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    lines.append([x, y])

# solve
lines.sort()
x_min, y_max = lines[0][0], lines[0][1]
length_total = y_max - x_min

for x, y in lines[1:]:
    if y_max < y:
        length_total += y - max(x, y_max)
        y_max = y

# print
print(length_total)
