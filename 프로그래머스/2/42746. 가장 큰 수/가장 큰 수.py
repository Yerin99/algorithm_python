from functools import cmp_to_key


def solution(numbers):
    def compare(a, b):
        if int(a + b) > int(b + a):
            return -1
        elif int (a + b) < int (b + a):
            return 1
        else:
            return 0
    
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    
    answer = ''.join(numbers)
    return str(int(answer))
