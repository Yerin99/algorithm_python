from itertools import product
from functools import cmp_to_key


def compare(x, y):
    aeiou = ['A', 'E', 'I', 'O', 'U']
    d = dict()

    for i in range(5):
        d[aeiou[i]] = i
    
    for i in range(min(len(x), len(y))):
        if d[x[i]] < d[y[i]]:
            return -1
        elif d[x[i]] > d[y[i]]:
            return 1
        else:
            continue
    
    return len(x) - len(y)


def solution(word):
    answer = 0
    aeiou = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    
    for i in range(1, 6):
        for e in product(aeiou, repeat=i):
            dictionary.append("".join(list(e)))
    
    dictionary.sort(key=cmp_to_key(compare))
    answer = dictionary.index(word) + 1
    
    return answer