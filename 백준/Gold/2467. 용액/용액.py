def two_pointer(front, back, solutions):
    min_sum = 2e9
    answer = (0, 0)

    while front < back:
        current_sum = solutions[front] + solutions[back]

        if abs(current_sum) < min_sum:
            min_sum = abs(current_sum)
            answer = (solutions[front], solutions[back])

        if current_sum < 0:
            front += 1
        else:
            back -= 1

    return answer


n = int(input())
solutions = list(map(int, input().split()))
front, back = 0, n - 1
print(*two_pointer(front, back, solutions))
