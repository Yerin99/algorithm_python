def is_matrix_too_small(n, m):
    return n < 3 or m < 3


def flip_matrix(a, i, j):
    for k in range(3):
        for l in range(3):
            a[i+k][j+l] ^= 1  # XOR 연산으로 0 <-> 1 변환


def check_matrix(a, b, n, m):
    result = 0

    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                result += 1
                flip_matrix(a, i, j)

    return result if a == b else -1


def main():
    n, m = map(int, input().split())

    a = [list(map(int, list(input().strip()))) for _ in range(n)]
    b = [list(map(int, list(input().strip()))) for _ in range(n)]

    if a == b:
        print(0)
    elif is_matrix_too_small(n, m):
        print(-1)
    else:
        print(check_matrix(a, b, n, m))


main()
