n = int(input())
is_prime = [False, False] + [True] * (n-1)

for num in range(2, n+1):
    if is_prime[num]:
        for x in range(num*2, n+1, num):
            is_prime[x] = False

prime_numbers = []

for num in range(2, n+1):
    if is_prime[num]:
        prime_numbers.append(num)

f, b = 0, 0
answer = 0
target = n
length = len(prime_numbers)

if prime_numbers:
    total = prime_numbers[0]

    while f < length:
        if total == target:
            answer += 1
            total -= prime_numbers[f]
            f += 1
        elif total > target:
            total -= prime_numbers[f]
            f += 1
        else:  # total < target
            if b < length - 1:
                b += 1
                total += prime_numbers[b]
            else:
                break

print(answer)