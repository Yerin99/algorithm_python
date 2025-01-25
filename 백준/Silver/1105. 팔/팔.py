L, R = input().split()

if len(L) != len(R):
    print(0)
else:
    count = 0
    for l_digit, r_digit in zip(L, R):
        if l_digit != r_digit:
            break
        if l_digit == '8':
            count += 1
    print(count)
