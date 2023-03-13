'''
[설명]
손님을 도착지로 데려다줄 때마다 연료가 충전
연료가 바닥나면 그 날의 업무가 끝
M명의 승객을 태우는 것이 목표
N×N
비어 있거나 벽. 0은 빈칸, 1은 벽.
상하좌우로 인접한 빈칸 중 하나로 이동
최단경로로 이동 -> BFS
M명의 승객, 이동
여러 승객이 같이 탑승하는 경우는 없음
한 승객을 태워 목적지로 이동시키는 일을 M번 반복
출발지에서만 택시에 탈 수 있고, 목적지에서만 택시에서 내릴 수 있음

- 승객 선택
    - 현재 위치에서 최단거리가 가장 짧은 승객 -> 출발지를 arr에 추가 기록 관리 -> arr(x,y) == 2
        - 그중 행 번호가 가장 작은 승객
            - 그중 열 번호가 가장 작은 승객 -> dxy 구성에 반영 -> heapq에 추가될 때 자동 반영

택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0

- 연료
    - 연료는 한 칸 이동할 때마다 1만큼 소모
    - 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전
    - 이동하는 도중에 연료가 바닥나면 이동에 실패. 종료.
    - 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 성공.

운전을 시작하는 칸은 빈칸
모든 출발지와 목적지는 빈칸
모든 출발지는 서로 다름
각 손님의 출발지와 목적지는 다름

[문제]
모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양
이동 도중에 연료가 바닥나서 다음 출발지나 목적지로 이동할 수 없으면 -1
모든 손님을 이동시킬 수 없는 경우 -1
'''
'''
[알고리즘]
- arr: 가장자리를 벽(1)으로 padding -> 범위 조건 제거 가능
- passenger
    - 관리용 dict() 구성. 검색 속도 효과적.
    - {(출발지): (목적지)}
- BFS
    - 변수: start_point, target_func
    - target_func
        - func_1
            - (lambda i, j: arr[i][j] == 2)
            - 운전자 출발지(시작점 or 이전 고객 도착지) ~ 가장 가까운 "고객"(고객 출발지) 선정
        - func_2
            - (lambda i, j: (i, j) == passenger[(start_i, start_j)])
            - 고객 출발지 ~ 고객 도착지까지 가장 가까운 "거리" 선정
    - dxy
        - 우선순위: 행이 작을 수록, 그다음 열이 작을 수록.
        - 우선순위를 반영한 dxy 구성 후 nxt 계산하여 heapq에 추가. 자동 반영 효과.
        - [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
'''
'''
[구조]
- arr 저장. 가장자리 벽(1)으로 padding
- for 승객 수:
    - 승객의 출발지 행과 열 번호, 목적지 행과 열 번호
    - passenger[(start_i, start_j)] = (end_i, end_j)
    - arr에 승객 출발지 2로 표기

- for 승객 수:
    - start_i, start_j, dist = BFS(운전 시작 지점, lambda 고객 출발지 모음) # 운전자 출발지 ~ 가장 가까운 고객까지 이동
    - if 잔여 연료가 거리보다 적다면:
        - stop_flag = -1
        - break
    - 이동 거리만큼 연료 감소
    - 기존 고객 시작 위치 0으로 변경

    - end_i, end_j, dist = BFS((고객 출발지), lambda 고객 도착지 모음) # 고객 출발지 ~ 고객 도착지까지 가장 가까운 dist 계산
    - if 잔여 연료가 거리보다 적다면:
        - stop_flag = -1
        - break
    - 거리만큼 연료 충전
    - 종료 위치를 드라이버 시작 위치로 변경

- stop_flag or 잔여 연료 F 출력

- BFS(start_point, target_func):
    - visited 초기화
    - while queue:
        - if target_func(i, j): 
            - 가장 가까운 지점 도착시 종료
                - func_1) 가장 가까운 고객
                - func_2) 고객 도착점까지의 가장 가까운 dist
            - return i, j, dist

        - for 4방향:
            - if 미방문 & 벽이 아니면:
                - 방문 처리
                - queue 추가 (dist + 1, ni, nj)

    - return 0, 0, F + 1 # (i, j, dist). 연료 부족 비정상 종료.
'''

import sys
from heapq import heappop, heappush

input_list = lambda dtype=int: [dtype(i) for i in sys.stdin.readline().strip().split()]


def BFS(start_point, target_func):
    queue = [(0, *start_point)]
    visited = [[False] * (N + 2) for _ in range(N + 2)]
    visited[start_point[0]][start_point[1]] = True

    while queue:
        dist, i, j = heappop(queue)
        if target_func(i, j): # 가장 가까운 지점 도착시 종료(1> 가장 가까운 고객, 2> 고객 도착점까지의 가장 가까운 dist)
            return i, j, dist

        for ni, nj in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
            if not visited[ni][nj] and arr[ni][nj] != 1: # 미방문 & 벽이 아니면.
                visited[ni][nj] = True
                heappush(queue, (dist + 1, ni, nj))

    return 0, 0, F + 1 # i, j, dist. dist > F 이므로, 종료 활성화.


N, M, F = map(int, input().split()) # arr 크기, 초기 연료량 F.
arr = [[1] * (N + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1] * (N + 2)] # 가장자리를 1로 padding. 1 은 벽.
T = list(map(int, input().split())) # 운전 시작하는 칸의 행, 열 번호
passenger = {}

for _ in range(M):
    start_i, start_j, end_i, end_j = map(int, input().split()) # 승객의 출발지 행과 열 번호, 목적지 행과 열 번호
    passenger[(start_i, start_j)] = (end_i, end_j)
    arr[start_i][start_j] = 2 # 승객 출발지 2로 표기

stop_flag = 0
for _ in range(M):
    start_i, start_j, dist = BFS(T, lambda i, j: arr[i][j] == 2) # 운전자 출발지 ~ 가장 가까운 고객까지 이동
    if dist > F:
        stop_flag = -1
        break
    F -= dist # 이동 거리만큼 연료 감소
    arr[start_i][start_j] = 0 # 고객 시작 위치 초기화

    end_i, end_j, dist = BFS((start_i, start_j), lambda i, j: (i, j) == passenger[(start_i, start_j)]) # 고객 출발지 ~ 고객 도착지까지 가장 가까운 dist 계산
    if dist > F:
        stop_flag = -1
        break
    F += dist
    T = (end_i, end_j) # 이전 고객 도착지를, 드라이버 시작지로 변경

print(stop_flag if stop_flag == -1 else F)