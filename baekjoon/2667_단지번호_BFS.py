from collections import deque

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]

dxy = [(1,0), (-1,0), (0,1), (0,-1)]

def BFS(x, y):
    global cnt
    q = deque([(x, y)])
    # q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dxy[i][0], y+dxy[i][1]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny]==1:
                    arr[nx][ny]=0
                    q.append((nx, ny))
                    cnt+=1

result = []
section = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        if 0<=i<N and 0<=i<N:
            if arr[i][j]==1:
                arr[i][j]=0
                section+=1
                cnt+=1
                BFS(i, j)
                result.append((section, cnt))

result.sort(key=lambda x: x[1])
print(len((result)))
for i in result:
    print(i[1])