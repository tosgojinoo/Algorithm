# pypy3 통과, python3 시간초과
# 최장거리 문제지만, 모든 케이스를 검색해야 하기 때문에, 적당한 가지치기 조건이 없는 경우 BFS로 풀이해야함

def DFS(y,x, memory):
    global result
    result = max(result, len(memory))
    for i in range(4):
        ny, nx = y+dxy[i][0], x+dxy[i][1]
        if 0<=ny<R and 0<=nx<C and arr[ny][nx] not in memory:
            DFS(ny, nx, memory+arr[ny][nx])

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
dxy = [(1,0), (-1,0), (0,1), (0,-1)]
memory = arr[0][0]
result = 0
DFS(0,0, memory)
print(result)
