from collections import deque
import sys


input = sys.stdin.readline
n = int(input())
deck = deque()

for _ in range(n):
    order = list(map(int, input().split()))
    o = order[0]

    if o == 1:
        deck.appendleft(order[1])
    elif o == 2:
        deck.append(order[1])
    elif o == 3:
        print(deck.popleft() if deck else -1)
    elif o == 4:
        print(deck.pop() if deck else -1)
    elif o == 5:
        print(len(deck))
    elif o == 6:
        print(0 if deck else 1)
    elif o == 7:
        print(deck[0] if deck else -1)
    elif o == 8:
        print(deck[-1] if deck else -1)
