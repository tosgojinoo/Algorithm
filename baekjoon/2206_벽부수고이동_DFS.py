# 풀지 못하는 경우를, 모든 case를 계산 후에 알 수 있는 경우 DFS를 적용하지 않음
# 시간/메모리 초과
import sys
sys.setrecursionlimit(10**6)

def DFS(y, x, chance):
    global result, visited
    if y==N and x==M:
        result = min(result, visited[chance][y][x])
        return
    for dy, dx in moves:
        ny, nx = y+dy, x+dx
        if 1<=ny<=N and 1<=nx<=M and visited[chance][ny][nx]==0:
            if arr[ny][nx]==0:
                visited[chance][ny][nx]=visited[chance][y][x]+1
                DFS(ny, nx, chance)
                visited[chance][ny][nx]=0
            elif arr[ny][nx]==1 and chance==1:
                chance-=1
                visited[chance][ny][nx] = visited[chance+1][y][x] + 1
                DFS(ny, nx, chance)
                visited[chance][ny][nx] = 0
                chance+=1
            # elif arr[ny][nx]==1 and chance==0: pass


N, M = map(int, input().split()) # N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)
arr = [[1]*(M+1)]
arr = arr + [[1]+list(map(int, list(input()))) for _ in range(N)]
visited = [[1]*(M+1)]
visited = [visited + [[1]+[0]*M for _ in range(N)] for _ in range(2)]
moves = [(1,0),(-1,0),(0,1),(0,-1)]

result = N*M*2 # 배열 크기의 최대 2배. because, 벅 허물고 난 후 전부 다시 돌 수도 있기 때문
visited[0][1][1] = 1
visited[1][1][1] = 1
arr[1][1] = 1

DFS(1,1,1) # y, x, chance
print(-1 if result == N*M*2 else result)

