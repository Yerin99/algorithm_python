import sys
input = sys.stdin.readline

m = int(input())
s = [0]*20

for _ in range(m):
    calculation = list(input().split())
    command = calculation[0]

    if command == "all":
        s = [1]*20
    elif command == "empty":
        s = [0]*20
    else:
        num = int(calculation[1]) - 1
        if command == "add":
            s[num] = 1
        elif command == "remove":
            s[num] = 0
        elif command == "check":
            print(s[num])
        elif command == "toggle":
            s[num] = (s[num] + 1) % 2
