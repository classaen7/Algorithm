import heapq

def solution(n, works):
    # 작업량이 없으면 피로도는 0
    if sum(works) <= n:
        return 0

    # 최대 힙을 사용하기 위해 음수 변환
    max_heap = [-work for work in works]
    heapq.heapify(max_heap)

    # 남은 시간을 소진하며 작업량 줄이기
    while n > 0:
        largest = -heapq.heappop(max_heap)  # 가장 큰 작업량 가져오기
        largest -= 1  # 작업량 1 감소
        heapq.heappush(max_heap, -largest)  # 다시 힙에 추가
        n -= 1

    # 남은 작업량으로 피로도 계산
    return sum(work ** 2 for work in map(lambda x: -x, max_heap))