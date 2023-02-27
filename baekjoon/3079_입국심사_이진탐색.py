import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # 입국심사대 개수, 인원
arr = [int(input()) for _ in range(N)]
left, right = min(arr), max(arr) * M
ans = right

while left <= right: # 양 끝단 기준점끼리 스위칭 되면 종료
    mid = (left + right) // 2
    # 새롭게 주어진 mid 시간 내 각각의 게이트에서 처리할 수 있는 인원의 총합
    total = list(map(lambda x: mid//x, arr))
    print(total)

    if sum(total) >= M:
        right = mid - 1 # 심사시간 줄이기
        ans = min(mid, ans) # 최소시간 저장
    else:
        left = mid + 1 # 심사시간 늘리기

print(ans)