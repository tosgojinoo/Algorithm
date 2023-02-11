''' my idea
BFS()
- queue = deque([start, 0])
- visited -> 3차원 필요
- key_info = list() -> x => 비트마스크 활용
- door_info = list()
- cnt = 0
- while queue:
    - y, x, cnt = queue.popleft()
    - for i in range(4):
        - ny, nx = y, x + dxy
        - if a[ny,nx] == '1': return cnt+1

        - if '.' or '0':
            - visited
            - queue.append((y, x, cnt+1))
        - if 소문자(키):
            - visited
            - arr[ny,nx] = '.'
            - key_info.append()
            - queue.append((y, x, cnt+1))
        - if 대문자(문) -> 소문자 in key_info:
            - arr[ny,nx] = '.'
            - visited reset
            - queue.append((y, x, cnt+1))

- print(-1)
- return

main
- arr 구성
    - start 저장(민식이 위치)

''''''
- *** 9328_열쇠와 다르게, key 개수가 정해져 있으므로 비트마스크 활용 필수
- *** visited[key bitmask][y][x]
- 보유 키 상태 변경시 큐 삽입
'''

from collections import deque

def BFS():
    x, y = start
    queue = deque([(x, y, 0, 0)])
    visited = [[[0] * 2**len("abcdef") for _ in range(M)] for _ in range(N)]
    visited[x][y][0] = True
    while queue:
        x, y, cnt, key = queue.popleft()
        if arr[x][y] == "1":
              return cnt
        else:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<N and 0<=ny<M and arr[nx][ny] != '#' and not visited[nx][ny][key]: # 범위 내, 벽 아님, 동일 키 상태일때 미방문.
                    if arr[nx][ny] == '.': # 빈칸
                        visited[nx][ny][key] = True
                        queue.append((nx, ny, cnt+1, key))
                    elif arr[nx][ny] == "1": # 출구
                        return cnt+1
                    elif arr[nx][ny] in "ABCDEF" and key & 1 << (ord(arr[nx][ny]) - 65): # 문, 보유키와 맞는지.
                        visited[nx][ny][key] = True
                        queue.append((nx, ny, cnt+1, key))
                    elif arr[nx][ny] in "abcdef" and not visited[nx][ny][key|(1 << ord(arr[nx][ny]) - 97)]: # 키, 동일 키 상태로 미방문.
                        visited[nx][ny][key | (1 << ord(arr[nx][ny]) - 97)] = True
                        queue.append((nx, ny, cnt+1, key | (1 << ord(arr[nx][ny]) - 97)))
    return -1


N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
start = None
for i in range(N):
    for j in range(M):
        if arr[i][j] == "0": # 민식이 위치
            arr[i][j] = '.' # 제거
            start = (i, j) # 저장

print(BFS())