a = [1]
r = 0
n = int(input())
for i in range(1, n+1):
    a.append(i*a[i-1])

for x in str(a[n])[::-1]:
    if x == '0':
        r += 1
    else:
        break
print(r)