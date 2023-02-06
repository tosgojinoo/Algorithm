# 인접 4칸 합 최대
# DFS, brute force o
# DP x
# 테트로미노 생성
#   - 4개까지 진전
#   - cnt 1일때 사방 추가 탐색
# visited
# DFS 종료 조건
#   - 모든 곳 방문시
# 제한 조건
#   - arr 영역 밖
#   - visited == 1

import sys
input = sys.stdin.readline

def DFS(y, x, cnt, total):
    global ans
    if ans >= total + max_val * (3 - cnt): # 종료 조건: 남은 횟수 * max_val + 현재값 이 ans 보다 작을때, 미리 종료.
        return
    if cnt == 3: # 종료 조건
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0: # 제한
                if cnt == 1: # ***** cnt 1일때만 1회 더 DFS. 'ㅏ' 모양 생성.
                    visited[ny][nx] = 1
                    DFS(y, x, cnt + 1, total + arr[ny][nx])
                    visited[ny][nx] = 0
                visited[ny][nx] = 1
                DFS(ny, nx, cnt + 1, total + arr[ny][nx])
                visited[ny][nx] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for y in range(N):
    for x in range(M):
        visited[y][x] = 1
        DFS(y, x, 0, arr[y][x])
        visited[y][x] = 0

print(ans)