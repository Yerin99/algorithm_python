import sys

input = sys.stdin.readline
s, p = input().rstrip(), input().rstrip()

print(1 if p in s else 0)
