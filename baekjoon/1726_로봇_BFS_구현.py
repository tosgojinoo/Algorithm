'''
[설명]
방향은 동, 서, 남, 북
로봇의 이동을 제어하는 명령어.
- 명령 1. Go k: k는 1, 2 또는 3일 수 있다. 현재 향하고 있는 방향으로 k칸 만큼 움직인다.
- 명령 2. Turn dir: dir은 left 또는 right 이며, 각각 왼쪽 또는 오른쪽으로 90° 회전한다.
공장 내 궤도가 설치되어 있는 상태가 아래와 같이 0과 1. -> arr[y][x] = 0 or 1
로봇에게 입력
0은 궤도가 깔려 있어 로봇이 갈 수 있는 지점이고, 1은 궤도가 없어 로봇이 갈 수 없는 지점
(y, x) 는 (1,1) ~ (N, M)

[문제]
로봇의 현재 위치와 바라보는 방향이 주어졌을 때,
로봇을 원하는 위치로 이동시키고,
원하는 방향으로 바라보도록 하는데
최소 몇 번의 명령이 필요
'''
'''
[알고리즘]
- 문제에서는 idx 1부터 시작 -> idx -1 shift 
- 최소 명령 == 최단 거리 -> BFS
- go/turn을 함수로 뺄 필요 없음(BFS 에서만 사용)
- BFS
    - 지점별로 방향 명령에 따라 전개 다름 -> visited[y][x][4방향] 설정
    - 우선순위 x, 개별적 cnt 기억 필요 -> queue = [(y, x, dir, cnt)]
    - 방향전환은 좌우 90도만 가능 -> change_dir 리스트 추가 구성하여, (idx==방향)별 전환 가능 방향 관리 
'''
'''
[구조]
- arr, 출발지, 목적지 입력
- BFS
    - visited 설정 
    - queue 설정
    - while queue
        - queue.popleft()
        - 종료 조건: (목표위치와 방향)에 도착. cnt 리턴.
        - 이동 (동일 방향 1~3배)
            - 가지치기: 벽 or 범위 밖(forward 1 부터 바로 확인 후 바로 탈출, break) 
            - 가지치기: 방문기록 있으면 무시(1~3 중 방문기록 유무에 따라 달리 적용, continue)
            - queue 추가(변경 좌표. ny, nx, nd, cnt+1)
            - 방문 처리(변경 좌표) 
        - 방향 전환
            - 가지치기: 방문기록
            - queue 추가(현재 좌표. y, x, nd, cnt+1)
            - 방문 처리(현재 좌표, 변경 방향)
'''

from sys import stdin
from collections import deque
input = stdin.readline

# 동 서 남 북
dy = (0, 0, 1, -1) # 동1, 서2, 남3, 북4
dx = (1, -1, 0, 0)
change_dir = ((2, 3), (2, 3), (0, 1), (0, 1)) # 동->남/북, 서->남/북, 남->동/서, 북->동/서

def BFS():
    visited = [[[0] * 4 for _ in range(N)] for _ in range(M)]
    visited[sy-1][sx-1][sd-1] = 1
    queue = deque([(sy-1, sx-1, sd-1, 0)])
    while queue:
        y, x, d, cnt = queue.popleft()
        if (y, x, d) == (gy-1, gx-1, gd-1): # (목표위치와 방향)에 도착하면 cnt 리턴
            return cnt

        for forward in range(1, 4): # 1~3 이동 가능
            ny = y + dy[d] * forward
            nx = x + dx[d] * forward
            nd = d
            if not (0 <= ny < M and 0 <= nx < N) or arr[ny][nx]: # 종료 조건: 벽 or 범위 밖
                break
            if visited[ny][nx][nd]: # 방문 기록 있을 경우 무시
                continue
            queue.append((ny, nx, nd, cnt+1))
            visited[ny][nx][nd] = 1

        # 방향 바꾸기
        for nd in change_dir[d]:
            if visited[y][x][nd]:
                continue
            queue.append((y, x, nd, cnt+1))
            visited[y][x][nd] = 1


M, N = map(int, input().split()) # 직사각형의 세로 길이 M과 가로 길이 N
arr = [list(map(int, input().split())) for _ in range(M)] # 궤도 설치 상태 (0 or 1)
sy, sx, sd = map(int, input().split()) # 로봇 출발 지점 위치, 방향
gy, gx, gd = map(int, input().split()) # 로봇 도착 지점 위치, 방향

print(BFS())