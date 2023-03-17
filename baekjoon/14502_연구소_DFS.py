'''
[설명]
N×M
연구소는 빈 칸, 벽

일부 칸은 바이러스가 존재
이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있음
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다. -> 경우의 수 DFS
0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳
바이러스가 퍼질 수 없는 곳을 안전 영역
2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수
빈 칸의 개수는 3개 이상

[문제]
얻을 수 있는 안전 영역의 최대 크기
'''
'''
[알고리즘]
- select_wall
    - 모든 칸 중에서, 브루트-포스로 벽 선택
    - 1열로 idx 구성한 후 적용
        - for idx in range(start, N * M): 
            - r = idx // M  # M으로 나눈 몫는 행
            - c = idx % M  # M으로 나눈 나머지는 열
            
- arr 에서 특정값 세기 
    - sum(row.count(0) for row in arr_copy) 

'''
'''
[구조]
- arr 저장
- dxy 상하좌우
- safe_region = 최대 안전 영역

select_wall(0,0)
print(safe_region)


# 벽 선택하기
- select_wall(start, cnt):
    - if cnt == 3: 
        # 벽이 선택된 그래프 복사
        - arr_copy = [arr[i][:] for i in range(N)]
        
        # DFS 로 바이러스 퍼뜨리기
        - for 전체 탐색:
            - if 바이러스:
                - DFS(i, j, arr_copy)
        - safe_cnt = sum(row.count(0) for row in arr_copy)
        - safe_region = max(safe_region, safe_cnt)
        - return

    - else: # 벽이 3개 선택되지 않은 경우
        # 브루트-포스로 벽 선택
        - for idx in range(start, N*M): 
            - r = idx를 M으로 나눈 몫
            - c = idx를 M으로 나눈 나머지
            - if 빈칸: 
                - arr[r][c] = 벽으로 선택
                - select_wall(idx, cnt+1) # 다음 벽 선택
                - arr[r][c] = 원복
                
- DFS(x, y, arr_copy):
    - arr_copy[x][y] = 2 # 바이러스로 변경

    # 상하좌우 탐색
    - for 4방:
        - if 범위 내:
            - if 빈칸: 
                - DFS(nx, ny, arr_copy)
'''

# DFS 보다 BFS 추천
import sys


# DFS
def DFS(x, y, arr_copy):
    arr_copy[x][y] = 2 # 바이러스로 변경

    # 상하좌우 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not arr_copy[nx][ny]: # 바이러스가 퍼질 수 있는 곳
                DFS(nx,ny,arr_copy) # 바이러스 퍼뜨리기


# 벽 선택하기
def select_wall(start, cnt):
    global safe_region, arr

    if cnt == 3: # 벽이 3개 선택된 경우 실행
        arr_copy = []
        for i in range(N):
            arr_copy.append(arr[i].copy())  # 벽이 선택된 그래프 복사
        # DFS 로 바이러스 퍼뜨리기
        for i in range(N):
            for j in range(M):
                if arr_copy[i][j] == 2: # 바이러스 발견시에 DFS
                    DFS(i, j, arr_copy)
        safe_cnt = sum(row.count(0) for row in arr_copy) # 안전 영역 개수 계산
        safe_region = max(safe_region, safe_cnt) # 최대 안전 영역 개수 갱신
        return

    else: # 벽이 3개 선택되지 않은 경우
        for idx in range(start, N*M): # 브루트-포스로 벽 선택
            r = idx // M # M으로 나눈 몫는 행
            c = idx % M # M으로 나눈 나머지는 열
            if not arr[r][c]: # 해당 구역이 0인 경우에
                arr[r][c] = 1 # 벽으로 선택
                select_wall(idx, cnt+1) # 다음 벽 선택
                arr[r][c] = 0 # 되돌리기


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] # 그래프 생성
dx, dy = [-1,1,0,0], [0,0,-1,1] # 상하좌우 이동
safe_region = 0 # 최대 안전 영역

select_wall(0, 0)
print(safe_region)

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

def DFS(cnt):
    global result
    if cnt == 3:
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
                    cnt+=1
                    DFS(cnt)
                    arr[i][j]=0
                    cnt-=1

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0]*m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

result=0
DFS(0)
print(result)
'''
