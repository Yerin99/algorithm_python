def count2(num):
    if num < 2:
        return 0

    count = 0

    while num >= 2:
        count += num // 2
        num //= 2

    return count


def count5(num):
    if num < 5:
        return 0

    count = 0

    while num >= 5:
        count += num // 5
        num //= 5

    return count


n, r = map(int, input().split())
num_of_two = count2(n) - count2(r) - count2(n-r)
num_of_five = count5(n) - count5(r) - count5(n-r)

print(min(num_of_two, num_of_five))
