def solution(numbers):
    numbers = list(map(str, numbers))
    # 핵심: 문자열을 반복하여 비교 기준을 만듦
    numbers.sort(key=lambda x: x*4, reverse=True)
    
    answer = ''.join(numbers)
    return '0' if answer[0] == '0' else answer
