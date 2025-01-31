import sys
import math
input = sys.stdin.readline

# 직선의 방향을 기약화하고 부호 규칙을 통일하는 함수
def canonical(dx, dy):
    """(dx, dy)를 gcd로 나누어 방향을 기약화하고
       부호 규칙을 통일(예: x>0이거나 x=0일 때 y>0)"""
    if dx == 0:
        return (0, 1)
    if dy == 0:
        return (1, 0)
    g = math.gcd(dx, dy)
    dx //= g
    dy //= g
    # x가 음수면 부호 뒤집고, x=0이면 y를 양수로
    if dx < 0:
        dx, dy = -dx, -dy
    elif dx == 0 and dy < 0:
        dy = -dy
    return (dx, dy)


def solve():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    answer = 0
    for i in range(N):
        freq = {}
        x0, y0 = points[i]
        # i번 점에서 다른 점들로 가는 벡터를 기약화하여 카운팅
        for j in range(N):
            if i == j:
                continue
            dx = points[j][0] - x0
            dy = points[j][1] - y0
            d = canonical(dx, dy)
            freq[d] = freq.get(d, 0) + 1

        # (dx, dy)에 대해 (dy, -dx)가 수직 방향
        # 각 빈도수의 곱만큼 직각삼각형이 생김
        for (dx, dy), cnt in freq.items():
            # 수직 벡터 구해서 동일한 기준으로 기약화
            pdx, pdy = canonical(dy, -dx)
            if (pdx, pdy) in freq:
                # (dx, dy) < (pdx, pdy)를 조건으로 잡아
                # 같은 쌍을 두 번 세지 않게 처리
                if (dx, dy) < (pdx, pdy):
                    answer += cnt * freq[(pdx, pdy)]

    print(answer)


if __name__ == "__main__":
    solve()
