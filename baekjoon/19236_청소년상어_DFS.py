'''
[설명]
4×4
(x, y) x는 행의 번호, y는 열의 번호
한 칸에는 물고기가 한 마리
각 물고기는 번호와 방향
번호는 1 ~ 16
두 물고기가 같은 번호를 갖는 경우는 없음
방향은 8가지 방향(상하좌우, 대각선) 중 하나

- 상어 init
    - (0, 0)에 있는 물고기를 먹음
    - (0, 0)에 들어감
    - 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같음

- 물고기 이동
    - 물고기는 번호가 작은 물고기부터 순서대로 이동
    - 물고기는 한 칸을 이동
    - 이동할 수 있는 칸
        - 빈 칸
        - 다른 물고기가 있는 칸
    - 이동할 수 없는 칸
        - 상어
        - 공간의 경계를 넘음
    - 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전
        - 이동할 수 있는 칸이 없으면 이동 x
        - 그 외의 경우에는 그 칸으로 이동
            - 물고기가 다른 물고기가 있는 칸으로 이동할 때
                - 서로의 위치를 바꾸는 방식

- 상어 이동
    - 상어는 방향에 있는 칸으로 이동
    - 한 번에 여러 개의 칸 이동
    - 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않음
    - if 상어가 물고기가 있는 칸으로 이동 -> 모든 방향 DFS
        - 그 칸에 있는 물고기를 먹고
        - 그 물고기의 방향을 소유
    - else:
        - 물고기가 없는 칸으로는 이동 불가
        - 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어남

- 물고기 이동 > 상어 이동 > 반복

[문제]
상어가 먹을 수 있는 물고기 번호의 합의 최댓값 -> DFS
'''
'''
[알고리즘]
- 8방향 적용: (d + add_d) % 8
'''
'''
[구조]
- 상어 이동 DFS

'''


def find_fish(fish_idx, arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j][0] == fish_idx:
                return i, j
    return -1, -1


def swap_all_fish(r, c, arr):
    for fish_idx in range(1, N * N + 1):
        fish_r, fish_c = find_fish(fish_idx, arr) # idx에 맞는 fish 좌표 확인
        if fish_r == fish_c == -1: # fish_idx 없으면 return -1,-1. 무시
            continue
        d = arr[fish_r][fish_c][1] # 찾은 fish의 방향
        for add_d in range(8): # fish 갈자리 보기
            nd = (d + add_d) % 8
            fish_nr = fish_r + dr[nd]
            fish_nc = fish_c + dc[nd]
            if not (0<=fish_nr<N) or not (0<=fish_nc<N): # 범위 밖 무시
                continue
            if fish_nr == r and fish_nc == c: # 상어자리 무시
                continue
            arr[fish_r][fish_c][1] = nd # 새롭게 얻은 방향 적용
            arr[fish_r][fish_c], arr[fish_nr][fish_nc] = arr[fish_nr][fish_nc], arr[fish_r][fish_c] # 자리 스위칭
            break


def DFS(r, c, sum_values, arr):
    global ans
    sum_values += arr[r][c][0] # fish_idx 누적
    ans = max(ans, sum_values)
    d = arr[r][c][1]  # fish 방향 -> 상어 방향 전이
    arr[r][c][0] = 0  # fish 삭제

    swap_all_fish(r, c, arr) # fish 위치 변경

    while True: # 동일 방향 내 갈수 있는 모든 위치로 이동 후 DFS
        r += dr[d] # 1배씩 증가
        c += dc[d]
        if not (0<=r<N) or not (0<=c<N): # 범위 밖 종료. 집으로.
            break
        if arr[r][c][0] == 0: # fish_idx 가 비어있을 경우 무시
            continue

        # tmp = []
        # for i in range(N):
        #     tmp.append([])
        #     for j in range(N):
        #         tmp[i].append(arr[i][j].copy())
        DFS(r, c, sum_values, [[c[:] for c in l] for l in arr]) # 3차원 복사 방법 주의


N = 4
dr = (-1, -1, 0, 1, 1, 1, 0, -1) # ↑, ↖, ←, ↙, ↓, ↘, →, ↗.
dc = (0, -1, -1, -1, 0, 1, 1, 1)

arr = [[] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split())) # "ai는 물고기의 번호, bi는 방향" x 4
    for j in range(N):
        arr[i].append([row[j * 2], row[j * 2 + 1] - 1]) # dir -1 shift

ans = 0
DFS(0, 0, 0, arr) # r, c, sum_values, arr

print(ans)