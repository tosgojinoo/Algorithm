# DFS + DP (Top-down + Recursion)
# 정당성 검토:
#   1) 전체 문제의 최적해 == 부분 문제의 최적해의 합
#   => 도착 지점까지 가는 경우의 수는 도착 지점이 아닌 임의의 점들에서 도착지점까지 가는 경우의 수를 합한 것과 동일
#   2) 메모이제이션 방법
#   => Top-down 방식(이전 결과의 연산을 다음 결과에 연쇄적으로 반영)
# 주의:
#   1) visited 초기값을 0으로 할 경우 시간 초과
#   2) visited 값
#       a. -1: 아예 가보지 않은 곳과 이전 합이 0인 곳을 구분 가능
#       b. 0: 가보지 않은 곳과 DP 합을 구분할 수 없음


# import sys
# sys.setrecursionlimit(10**6)

def DFS_DP(y, x):
    global visited

    # 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
    if y==M-1 and x==N-1: return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴, DFS 종료
    if visited[y][x] != -1: return visited[y][x]

    cnt=0
    for dy, dx in moves:
        ny, nx = y+dy, x+dx
        if 0<=ny<M and 0<=nx<N and arr[ny][nx]<arr[y][x]:
            # DP 부분
            cnt += DFS_DP(ny, nx)

    visited[y][x] = cnt
    return visited[y][x]


# 세로의 크기 M과 가로의 크기 N
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
moves = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[-1]*N for _ in range(M)]
print(DFS_DP(0,0))
# print(visited)