import heapq

def solution(jobs):
    jobs.sort()  # 요청시각 기준 정렬
    n = len(jobs)
    time, idx, total = 0, 0, 0
    wait_queue = []

    while idx < n or wait_queue:
        # 현재 시간까지 들어온 작업 대기열에 추가
        while idx < n and jobs[idx][0] <= time:
            start, length = jobs[idx]
            heapq.heappush(wait_queue, (length, start))
            idx += 1
        
        if wait_queue:
            length, start = heapq.heappop(wait_queue)
            time += length
            total += time - start  # 반환 시간 누적
        else:
            # 대기열이 비었으면 다음 작업 시간으로 점프
            time = jobs[idx][0]

    return total // n
