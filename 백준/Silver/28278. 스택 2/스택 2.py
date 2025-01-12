import sys

input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    order = list(map(int, input().split()))
    o = order[0]
    if o == 1:
        stack.append(order[-1])
    elif o == 2:
        print(stack.pop() if stack else -1)
    elif o == 3:
        print(len(stack))
    elif o == 4:
        print(0 if stack else 1)
    elif o == 5:
        print(stack[-1] if stack else -1)