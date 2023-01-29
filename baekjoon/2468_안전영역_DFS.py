# https://www.acmicpc.net/problem/2468
import sys
# 재귀 제한 해제
sys.setrecursionlimit(10**6)
dxy = [(0,1), (0,-1), (1,0), (-1,0)]


def DFS(x, y):
    for i in range(4):
        nx, ny = x+dxy[i][0], y+dxy[i][1]

        if 0<=nx<N and 0<=ny<N and arr[nx][ny]>height and visited[nx][ny]==0:
            visited[nx][ny] = 1
            DFS(nx, ny)

N = int(input())
max_num = 0
result = 1

arr = [list(map(int, input().split())) for _ in range(N)]
max_num = max(map(max, arr))

for height in range(max_num):
    visited = [[0]*N for _ in range(N)]
    cnt = 0

    for i in range(N): # 행
        for j in range(N): # 열
            if arr[i][j] > height and visited[i][j] == 0:
                visited[i][j] = 1
                cnt += 1
                DFS(i, j)
    result = max(result, cnt)

print(result)


# # 위 코드 대비 시간이 2배 이상 소요됨
# def DFS(x, y):
#     if x < 0 or x >= N or y < 0 or y >= N or arr[x][y] <= height:
#         return
#
#     if visited[x][y] == 0:
#         visited[x][y] = 1
#         for i in range(4):
#             nx, ny = x+dxy[i][0], y+dxy[i][1]
#             DFS(nx, ny)
#
# N = int(input())
# max_num = 0
# result = 1
#
# arr = [list(map(int, input().split())) for _ in range(N)]
# max_num = max(map(max, arr))
#
# # 모든 높이에 대해 확인, 해당 높이보다 높은 경우를 모두 cnt
# for height in range(max_num):
#     visited = [[0]*N for _ in range(N)]
#     cnt = 0
#
#     for i in range(N): # 행
#         for j in range(N): # 열
#             if arr[i][j] > height and visited[i][j] == 0:
#                 cnt += 1
#                 DFS(i, j)
#     result = max(result, cnt)
#
# print(result)
