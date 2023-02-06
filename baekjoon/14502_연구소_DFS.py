# DFS 보다 BFS 추천


''' case 1
import sys

# 바이러스 전파
def DFS_virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and tmp[nx][ny]==0:
            tmp[nx][ny]=2
            DFS_virus(nx, ny)

#안전영역 개수 구하기
def Count():
    cnt=0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt+=1
    return cnt

def DFS(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = arr[i][j]

        for i in range(n):
            for j in range(m):
                if tmp[i][j]==2:
                    DFS_virus(i,j)
        result = max(result, Count())
        return
    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    arr[i][j]=1
                    count+=1
                    DFS(count)
                    arr[i][j]=0
                    count-=1

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0]*m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

result=0
DFS(0)
print(result)
'''

'''case2'''
# DFS 보다 BFS 추천
import sys


# DFS
def DFS(x,y,sel_wall):
    sel_wall[x][y] = 2 # 바이러스로 변경

    # 상하좌우 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if sel_wall[nx][ny] == 0: # 바이러스가 퍼질 수 있는 곳
                DFS(nx,ny,sel_wall) # 바이러스 퍼뜨리기


# 벽 선택하기
def select_wall(start, count):
    global safe_region, arr

    if count == 3: # 벽이 3개 선택된 경우 실행
        sel_wall = []
        for i in range(N):
            sel_wall.append(arr[i].copy())  # 벽이 선택된 그래프 복사
        # DFS 로 바이러스 퍼뜨리기
        for i in range(N):
            for j in range(M):
                if sel_wall[i][j] == 2: # 바이러스 발견시에 DFS
                    DFS(i,j,sel_wall)
        safe_count = sum(_.count(0) for _ in sel_wall) # 안전 영역 개수 계산
        safe_region = max(safe_region,safe_count) # 최대 안전 영역 개수 갱신
        return

    else: # 벽이 3개 선택되지 않은 경우
        for i in range(start, N*M): # 브루트-포스로 벽 선택
            r = i // M # M으로 나눈 몫는 행
            c = i % M # M으로 나눈 나머지는 열
            if arr[r][c] == 0: # 해당 구역이 0인 경우에
                arr[r][c] = 1 # 벽으로 선택
                select_wall(i,count+1) # 다음 벽 선택
                arr[r][c] = 0 # 되돌리기


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)] # 그래프 생성
dx, dy = [-1,1,0,0], [0,0,-1,1] # 상하좌우 이동
safe_region = 0 # 최대 안전 영역

select_wall(0,0)
print(safe_region)
