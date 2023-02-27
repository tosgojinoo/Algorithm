from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
house = []
chick = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: # 집
            house.append((i, j))
        elif arr[i][j] == 2: # 치킨집
            chick.append((i, j))

res = 1e9
for case in combinations(chick, m):
    tmp = 0
    for hx, hy in house:
        mini = 1e9
        for cx, cy in case:
            mini = min(mini, abs(hx - cx) + abs(hy - cy))
        tmp += mini
    res = min(res, tmp) # 누적 직선거리 최소값 출력
print(res)