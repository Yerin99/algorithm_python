import sys
import string
from collections import defaultdict


# input
input = sys.stdin.readline
s = input()
q = int(input())
questions = []

for _ in range(q):
    questions.append(input().split())

# solve
n = len(s)
total_dict = defaultdict(list)

for alphabet in string.ascii_lowercase:
    total = 0
    for i in range(n):
        char = s[i]
        if char == alphabet:
            total += 1
        total_dict[alphabet].append(total)

for question in questions:
    alphabet, start, finish = question
    start, finish = int(start), int(finish)
    result = total_dict[alphabet][finish]

    if start > 0:
        result -= total_dict[alphabet][start-1]

    # print
    print(result)
