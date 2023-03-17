'''
[설명]
- 규칙
    - 5×5 크기의 판이 5개
    - 이중 일부 칸은 참가자가 들어갈 수 있고 일부 칸은 참가자가 들어갈 수 없다.
    - 하얀 칸은 참가자가 들어갈 수 있는 칸
    - 검은 칸은 참가자가 들어갈 수 없는 칸
    - 참가자는 주어진 판들을 시계 방향, 혹은 반시계 방향으로 자유롭게 회전 -> DFS(경우의 수)
    - 판을 뒤집을 수는 없음
    - 회전을 완료한 후 참가자는 판 5개를 쌓음
    - 판을 쌓는 순서는 참가자가 자유롭게 정할 수 있음
    - 입구는 정육면체에서 참가자가 임의로 선택한 꼭짓점에 위치한 칸
    - 출구는 입구와 면을 공유하지 않는 꼭짓점에 위치한 칸
    - 참가자는 현재 위치한 칸에서 면으로 인접한 칸이 참가자가 들어갈 수 있는 칸인 경우 그 칸으로 이동
    - 미로의 입구 혹은 출구가 막혀있거나, 입구에서 출구에 도달할 수 있는 방법이 존재하지 않을 경우에는 탈출이 불가능

[문제]
미로를 탈출하는 가장 적은 이동 횟수를 출력 -> BFS(최소 이동)
탈출이 불가능할 경우에는 -1
'''
'''
[알고리즘]
- arr_init: 제공된 값 저장
- arr: arr 경우의 수 case 저장

- dxy 
    - 블록 회전이 아닌, 참가자 이동에 대한 dxy
    - 3차원에 맞게 dx, dy, dh 준비
    - 상하좌우앞뒤 6방향 이동
    - 단위백터이기 때문에 해당 차원 외 다른 차원들은 전부 0 이어야함
    - dh = (0, 0, 0, 0, 1, -1)
    - dy = (0, 0, 1, -1, 0, 0)
    - dx = (1, -1, 0, 0, 0, 0)

- solve
    - 판 쌓는 순서 중복순열 -> DFS

- permutation
    - 대상은 0~4
    - 밑판은 회전하나 안하나 동일하기 때문에 제외
    
- DFS
    - 5 x 5 x 5 블록의 배열에 대한 경우의 수 생성 필요
    - arr(0,0,0) == 1 일때, DFS(step+1) 거치고
    - 층별로 90도씩 회전 시키며 경우의 수 생성
    - step == 5 & arr(4,4,4)==1 일때, BFS
    
- BFS
    - 시작 ~ 끝 이동횟수 계산
    - visitied 는 visited & cnt
    - 이동거리
        - 모든 경우의 수에서 가장 짧은 이동거리는 12(높이 4 + 세로 4 + 가로 4)
        - result 가 12를 갖게 되면, exit() 프로그램 종료
        - visited에 이동거리 저장

'''
'''
[구조]
- arr_init = 저장 # 5 x 5 x 5.  0은 참가자가 들어갈 수 없는 칸, 1은 참가자가 들어갈 수 있는 칸
- arr = 경우의 수 저장

- dh = (0, 0, 0, 0, 1, -1)
- dy = (0, 0, 1, -1, 0, 0)
- dx = (1, -1, 0, 0, 0, 0)

- solve()

- solve(): 
    - for permutation([0~4], 5):
        - arr = arr_init 복사
        - DFS(0)

- permutation(arr, r)

- DFS(step): # 시작과 끝 조건만 부합하는 case 생성 -> BFS
    - if step == 5:
        - if arr[4][4][4]: # (4,4,4) 이 참가자가 들어갈 수 있 칸인 경우
            - BFS(arr)
        - return

    - for 4번 회전: 맨 윗판
        - if arr[0][0][0]: # (0,0,0) 이 참가자가 들어갈 수 있 칸인 경우
            - DFS(step + 1)
        - arr[step] = rotate(arr[step]) # 90도 회전하며 다음 경우의 수 생성

- rotate(arr_one):
    - tmp = 5 x 5 초기화
    - for arr_one 전체 탐색:
        - +90도 회전

    - return tmp
    

- BFS(arr):  # 시작부터 끝까지 이동
    - visited = arr 동일 크기, init 0
    
    - while queue:
        - if 종료지점:
            - result = min(result, visited[4][4][4])
            - if result == 12: # 가장 짧은 경로
                - exit() 선 종료
            - return

        - for 6방향:
            - nh/y/x = h/y/x + dh/y/x[i]
            
            - if 범위 내 아닐 경우: 무시
            - elif 방문했거나, 갈 수 없는 곳: 무시
            
            - queue 추가 (nh, ny, nx)
            - visited[nh][ny][nx] = visited[h][y][x] + 1
'''


# visited. 3차원. [수직층][y][x]
# cnt
# state. N개. 각 층별 회전 횟수 -> x
# rotate() 회전시 해당층 재배열
# 층별로 회전은 DFS -> 그냥 각 층 회전하며 루프
# 최소 이동 BFS
# 이동은 상하를 포함한 6방향
# 판 쌓는 순서 조합. yield로 구성

import sys
from collections import deque

def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in permutation(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + nxt

def rotate(arr_one):
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(len(arr_one)):
        for j in range(len(arr_one[0])):
            tmp[j][4 - i] = arr_one[i][j]

    return tmp

def BFS(arr):  # 시작부터 끝까지 이동
    global result
    visited = [[[0, 0, 0, 0, 0] for _ in range(5)] for _ in range(5)] # visitied == visited & cnt
    queue = deque([(0, 0, 0)])

    while queue:
        h, y, x = queue.popleft()
        if (h, y, x) == (4, 4, 4):
            result = min(result, visited[4][4][4])
            if result == 12: # 가장 짧은 경로의 경우 출력 후 종료
                print(result)
                exit()
            return

        for i in range(6):
            nh = h + dh[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= nh < 5) or not (0 <= ny < 5) or not (0 <= nx < 5): # 제한 조건: 범위
                continue
            elif not arr[nh][ny][nx] or visited[nh][ny][nx]: # 제한 조건: 방문했거나, 갈 수 없는 곳
                continue
            queue.append((nh, ny, nx))
            visited[nh][ny][nx] = visited[h][y][x] + 1

def DFS(step): # 시작과 끝 조건만 부합하는 case 생성 -> BFS
    global arr
    if step == 5:
        if arr[4][4][4]: # (4,4,4) 가 종료 조건에 만족하면
            BFS(arr)
        return

    for i in range(4):
        if arr[0][0][0]: # (0,0,0) 이 시작 조건에 만족하는 모든 경우에 DFS
            DFS(step + 1)
        arr[step] = rotate(arr[step]) # 회전하며 다음 경우의 수 생성

def solve(): # 판 쌓는 순서 조합 생성 -> DFS
    for d in permutation([0, 1, 2, 3, 4], 5): # 판 쌓는 순서 조합
        for i in range(5):
            arr[d[i]] = arr_init[i]
        DFS(0)


arr_init = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)] # 5 x 5 x 5.  0은 참가자가 들어갈 수 없는 칸, 1은 참가자가 들어갈 수 있는 칸
arr = [[[0] * 5 for _ in range(5)] for _ in range(5)]
result = sys.maxsize

# 상하좌우앞뒤 6방향 이동
dh = (0, 0, 0, 0, 1, -1)
dy = (0, 0, 1, -1, 0, 0)
dx = (1, -1, 0, 0, 0, 0)
solve()

if result == sys.maxsize:
    result = -1
print(result)