import sys
sys.setrecursionlimit(10**6)

dxy = [(1,0),(-1,0),(0,1),(0,-1)]

def DFS(y, x):
    for i in range(4):
        ny, nx = y+dxy[i][0], x+dxy[i][1]
        if 0<=ny<N and 0<=nx<M and arr[ny][nx]==1:
            arr[ny][nx]=0
            DFS(ny, nx)

T = int(input())

for tc in range(T):
    # 가로길이 M(1 ≤ M ≤ 50)
    # 세로길이 N(1 ≤ N ≤ 50)
    # 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    # print(arr)

    cnt = 0
    for i in range(N):
        for j in range(M):
           if arr[i][j]==1:
               arr[i][j]=0
               cnt+=1
               DFS(i, j)

    print(cnt)