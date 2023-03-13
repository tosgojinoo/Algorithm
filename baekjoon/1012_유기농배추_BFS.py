'''
[설명]
'단지번호 입력'과 유사

어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면
이 지렁이는 인접한 다른 배추로 이동
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접

배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로
서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 -> BFS
총 몇 마리의 지렁이가 필요한지 알 수 있다.

0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅
[문제]
'''
'''
[알고리즘]
- BFS
    - visited 사용 대신, arr(y,x) == 0 으로 처리
    - BFS 한번 진입하면 cnt++
'''
'''
[구조]

'''

from collections import deque

dxy = [(1,0),(-1,0),(0,1),(0,-1)]

def BFS(y, x):
    queue = deque([(y, x)])

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dxy[i][0], x+dxy[i][1]
            if 0<=ny<N and 0<=nx<M and arr[ny][nx]:
                arr[ny][nx]=0
                queue.append((ny, nx))


for _ in range(int(input())):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추 개수
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
               arr[i][j] = 0
               cnt += 1
               BFS(i, j)

    print(cnt)