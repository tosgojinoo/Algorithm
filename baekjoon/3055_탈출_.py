''' my idea
# 5427과 차이점
    - 5427: 도착지가 1개가 아님
    - 3055: 도착지가 1개
BFS
- queue = deque([sx,sy,0])
- water = deque([wx,wy,0])
- visited
- cnt = 0
- while queue:
    - wx, xy, cnt = water.popleft()
    - for i in range(4):
        - nwx, nwy = wxy + dxy
        - if 0<=nwx/nwy<N/M:
            - if 고슴도치로 변경할 대상:
            - if 물로 변경할 대상:


main
- arr
    - if '*':
        - wx, xy
    - if 'S':
        - sx, xy
'''
''' my idea
-> 불만 우선 실행할 경우 시간초과 가능성 있음 => 한 time에 불, 고슴도치 둘다 계산 필요
1. 불만 BFS
    - memory에 min(level) 저장
2. 상근 BFS
    - not 0<=(y,x)<N 이면, print(level)
    - (y,x)에 도착시
        - level >= memory[y][x] 면 print("impossible")
        - 아니면, continue
'''

'''
BFS
- 불 이동 계산
    - arr 직접 변경
- 고슴도치 이동 계산
    - visited 저장
'''

from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    while queue:
        x, y = queue.popleft()
        if arr[Dx][Dy] == 'S': # 도착지에 고슴도치 도착했다는 의미
            return visited[Dx][Dy]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if (arr[nx][ny] == '.' or arr[nx][ny] == 'D') and arr[x][y] == 'S': # (빈칸 or 도착지) and 고슴도치
                    arr[nx][ny] = 'S' # 고슴도치로 덮어쓰기
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
                elif (arr[nx][ny] =='.' or arr[nx][ny] =='S') and arr[x][y] == '*': # (빈칸 or 고슴도치) and 물
                    arr[nx][ny] = '*' # 물로 덮어쓰기
                    queue.append((nx,ny))
    return "KAKTUS"


R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()

for x in range(R):
    for y in range(C):
        if arr[x][y] == 'S': # 고슴도치 위치 부터 저장
            queue.append((x, y))
        elif arr[x][y] == 'D':
            Dx, Dy = x, y

for x in range(R):
    for y in range(C):
        if arr[x][y] == '*': # 물 위치 저장
            queue.append((x,y))

print(BFS())