n = int(input())

# 에라토스테네스의 체를 사용하여 소수 찾기
is_prime = [False, False] + [True] * (n - 1)  # 인덱스 0과 1은 소수가 아니므로 False로 시작

for num in range(2, n + 1):
    if is_prime[num]:
        for x in range(num * 2, n + 1, num):
            is_prime[x] = False

# 소수 리스트 생성
prime_numbers = [num for num in range(2, n + 1) if is_prime[num]]

# 투 포인터를 사용하여 연속된 소수들의 합으로 n을 만드는 경우의 수를 찾기
answer = 0
length = len(prime_numbers)
target = n

f = 0
total = 0

for b in range(length):
    total += prime_numbers[b]

    while total > target and f <= b:
        total -= prime_numbers[f]
        f += 1

    if total == target:
        answer += 1

print(answer)
