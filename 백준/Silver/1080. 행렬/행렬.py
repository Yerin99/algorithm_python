def is_a_and_b_same(a, b, n, m):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True


def is_matrix_too_small(n, m):
    return n < 3 or m < 3


def flip_zero_and_one(x):
    return (x + 1) % 2


def flip_matrix(a, b, n, m):
    result = 0

    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                for k in range(3):
                    for l in range(3):
                        a[i+k][j+l] = flip_zero_and_one(a[i+k][j+l])
                result += 1

            if is_a_and_b_same(a, b, n, m):
                return result

    return -1


def main():
    n, m = map(int, input().split())

    a = [list(map(int, list(input()))) for _ in range(n)]
    b = [list(map(int, list(input()))) for _ in range(n)]


    if is_a_and_b_same(a, b, n, m):
        print(0)
    elif is_matrix_too_small(n, m):
        print(-1)
    else:
        print(flip_matrix(a, b, n, m))



main()
