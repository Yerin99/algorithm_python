n = int(input())
a, b, c = 0, 1, -1
num = 1000000
p = 15 * (num // 10)
fin = (n+1) % p

if n == 0:
    print(a)
elif n == 1:
    print(b)
else:   
    for i in range(2, fin):
        c = (a % num + b % num) % num
        a, b = b, c

    print(c)
