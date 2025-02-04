def shoelace_formula(n, points):
    result = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % n]
        result += (x1*y2 - x2*y1)

    return round(abs(result)/2, 1)


def input_data():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    return n, points


def __main__():
    n, points = input_data()
    print(shoelace_formula(n, points))


__main__()
