from itertools import permutations


def make_prime_number_table(n):
    is_prime = [False, False] + [True] * (n-1)

    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    
    return is_prime


def solution(numbers):
    answer = 0
    max_num = int(''.join(sorted(numbers, reverse=True)))
    is_prime = make_prime_number_table(max_num)
                  
    for length in range(1, len(numbers)+1):
        for entry in set(permutations(numbers, length)):
            num = int(''.join(list(entry)))
            
            if len(str(num)) == length:
                print(num, is_prime[num])

                if is_prime[num]:
                    answer += 1

    return answer