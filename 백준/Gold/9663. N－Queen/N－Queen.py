def backtrack(row, used_cols, used_diag1, used_diag2, n, result):
    # row가 n이 되었다면 모든 행에 퀸을 놓았다는 뜻
    if row == n:
        result[0] += 1
        return

    for col in range(n):
        # 왼쪽 대각선 인덱스 (음수 방지 위해 + (n-1))
        d1 = row - col + (n - 1)
        # 오른쪽 대각선 인덱스
        d2 = row + col

        # 이미 사용 중(퀸이 놓여 있음)인 열/대각선이면 스킵
        if used_cols[col] or used_diag1[d1] or used_diag2[d2]:
            continue

        # 현재 col에 퀸을 놓는다고 가정하고 체크
        used_cols[col] = True
        used_diag1[d1] = True
        used_diag2[d2] = True

        # 다음 행으로 넘어감
        backtrack(row + 1, used_cols, used_diag1, used_diag2, n, result)

        # 백트래킹 - 원상 복구
        used_cols[col] = False
        used_diag1[d1] = False
        used_diag2[d2] = False


def solve_n_queens(n):
    # 열, 대각선 사용 여부를 저장할 불리언 리스트
    used_cols = [False] * n
    used_diag1 = [False] * (2 * n - 1)
    used_diag2 = [False] * (2 * n - 1)

    # 결과(해답 개수) 기록용
    result = [0]

    # 0번 행부터 시작
    backtrack(0, used_cols, used_diag1, used_diag2, n, result)

    return result[0]


def main():
    n = int(input().strip())
    print(solve_n_queens(n))


if __name__ == "__main__":
    main()
