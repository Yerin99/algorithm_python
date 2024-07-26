string1, string2 = input(), input()
n1, n2 = len(string1), len(string2)

cursor = 0
lcs = [[0]*(n2+1) for _ in range(n1+1)]

for i in range(n1+1):
    for j in range(n2+1):
        if i == 0 or j == 0:
            lcs[i][j] = 0
        elif string1[i-1] == string2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[n1][n2])
