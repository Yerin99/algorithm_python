import sys
import string

def solve():
    input = sys.stdin.readline
    S = input().strip()        # 문자열 입력
    q = int(input().strip())   # 쿼리(질문)의 개수

    # 1) 알파벳별 누적합(prefix sum)을 저장할 자료구조
    #    prefix[ch][i] = 문자열 S에서
    #    0번째 문자부터 (i-1)번째 문자까지 ch가 몇 번 등장하는가?
    n = len(S)
    prefix = {ch: [0] * (n + 1) for ch in string.ascii_lowercase}

    # 2) 문자열 한 번만 순회하며 알파벳별 누적합 생성
    for i, ch in enumerate(S):
        for alpha in string.ascii_lowercase:
            # 이전까지의 합을 그대로 복사
            prefix[alpha][i+1] = prefix[alpha][i]
        # 현재 문자가 alpha와 같으면 카운트 추가
        prefix[ch][i+1] += 1

    # 3) 쿼리 처리
    results = []
    for _ in range(q):
        alpha, l, r = input().split()
        l, r = int(l), int(r)
        # 구간 [l, r]에서 alpha의 개수 = prefix[alpha][r+1] - prefix[alpha][l]
        count_alpha = prefix[alpha][r+1] - prefix[alpha][l]
        results.append(str(count_alpha))

    # 4) 결과 출력
    print("\n".join(results))

# 직접 실행을 원하시면 아래 주석을 해제하고 사용하세요.
if __name__ == "__main__":
    solve()
