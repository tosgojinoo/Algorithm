# N x N, 상하좌우 이동, 이동 조건은 이전 지역보다 대나무가 많을 것
# 최대한 많은 칸 방문
# DFS & DP 문제

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[-1] * N for _ in range(N)]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 0


def DFS_DP(y, x):
    if DP[y][x] == -1:
        DP[y][x] = 0 # 일단 방문하게되면 DP는 0으로 갱신

        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if N > ny >= 0 and N > nx >= 0 and arr[ny][nx] > arr[y][x]:
                DP[y][x] = max(DP[y][x], DFS(ny, nx)) # DFS 계속 탐색하며 max 값 확인

    return DP[y][x] + 1 # 자기자신 추가


for i in range(N):
    for j in range(N):
        ans = max(ans, DFS(i, j))

print(ans)
# print(DP)