'''
[설명]
N×N크기
사탕의 색이 다른 인접한 두 칸 -> 브루트 포스(모든 범위 0~N-2) -> 상하/좌우 교환 -> 계산 -> 원복 (visited 필요 없음)
고른 칸에 들어있는 사탕을 서로 교환
모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 -> 브루트포스 -> 아래, 오른쪽으로 이동하는 모든 경우 계산 -> 재방문x -> BFS/DFS x
그 사탕을 모두 먹는다.
빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y

[문제]
상근이가 먹을 수 있는 사탕의 최대 개수
'''
'''
[알고리즘]
- 브루트포스
    - 인접한 두칸 -> 범위 0~N-2
    - 교환 -> 상하/좌우 교환
    - 범위 탐색 -> 교환 -> 최대 cnt 계산 -> 원복 (visited 미사용)
    - 행/열 단일 방향 연속 부분 -> 재방문 x -> 아래/오른쪽 이동 경우만 계산 -> BFS/DFS x
'''
'''
[구조]
- arr 입력
- y/x 탐색
    - if x < N-1
        - 두색 교환
        - ans = max(ans, check(arr))
        - 원복
    - if y < N-1 
        - 두색 교환
        - ans = max(ans, check(arr))
        - 원복

- check
    - for y (0 ~ N-1)
        - cnt 1
        - for x (0 ~ N-1)
            - if 오른쪽과 동일하면
                - cnt += 1
            - 아니면 cnt 리셋
            - res 최대값 저장
        - cnt 1
        - for x (0 ~ N-1)
            - if 아래쪽과 동일하면
                - cnt += 1
            - 아니면 cnt 리셋
            - res 최대값 저장
    return res            
'''


# 최대 개수 세기
def check(arr):
    res = 0
    for y in range(N):
        cnt = 1 # 자기 자신
        for x in range(N):
            if arr[y][x] == arr[y][x+1]: # 같은 색일 경우. 오른쪽 방향
                cnt += 1
            else: # 아니면 리셋
                cnt = 1
            res = max(res, cnt)
        cnt = 1
        for x in range(N):
            if arr[x][y] == arr[x+1][y]: # 같은 색일 경우. 아래 방향
                cnt += 1
            else: # 아니면 리셋
                cnt = 1
            res = max(res, cnt)
    return res


N = int(input())
arr = [list(input()) for _ in range(N)]
ans = 1

for y in range(N):
    for x in range(N): # 모든 지점을 탐색하며, 0~N-2 구간에서 두 색 교환
        if x < N - 1:
            arr[y][x], arr[y][x + 1] = arr[y][x + 1], arr[y][x] # 두 색 교환
            ans = max(ans, check(arr))
            arr[y][x], arr[y][x + 1] = arr[y][x + 1], arr[y][x] # 원복

        if y < N - 1:
            arr[y][x], arr[y + 1][x] = arr[y + 1][x], arr[y][x] # 두 색 교환
            ans = max(ans, check(arr))
            arr[y][x], arr[y + 1][x] = arr[y + 1][x], arr[y][x] # 원복
print(ans)