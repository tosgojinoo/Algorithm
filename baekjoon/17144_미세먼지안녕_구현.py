# 미세먼지 안녕!
import sys
input = sys.stdin.readline


def spread():
    new_arr = [[0]*C for _ in range(R)] # spread 된 것을 재분배하면 안되기 때문에, 새롭게 arr 구성 후 업데이트가 편리함.
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0: # 먼지
                prev = arr[i][j] # 최초값 저장
                spr = prev//5 # 단위 분배량
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0<=ni<=R-1 and 0<=nj<=C-1 and arr[ni][nj] != -1:
                        new_arr[ni][nj] += spr
                        prev -= spr
                new_arr[i][j] += prev
            elif arr[i][j] == -1: # 공청기
                new_arr[i][j] = -1 # 공청기 위치
    return new_arr


def purify():
    # 공청기 위치 확인. 윗 좌표.
    for purifier in range(R):
        if arr[purifier][0] == -1:
            break

    for i in range(purifier-1, 0, -1): # 공청기 열. 바로 윗 부분. 아래로 1칸씩
        arr[i][0] = arr[i-1][0]
    for j in range(C-1): # 0번 행. 왼쪽으로 1칸씩
        arr[0][j] = arr[0][j+1]
    for i in range(purifier): # 마지막 행. 공청기 윗쪽. 위로 1칸씩
        arr[i][C-1] = arr[i+1][C-1]
    for j in range(C-1, 1, -1): # 공청기 윗 행. 오른쪽 1칸씩
        arr[purifier][j] = arr[purifier][j-1]
    arr[purifier][1] = 0 # 공청기 중 위에서 나온 곳
    purifier += 1 # 공청기 두칸 중 아래칸
    for i in range(purifier+1, R-1): # 공청기 열. 바로 아랫 부분.
        arr[i][0] = arr[i+1][0]
    for j in range(C-1): # 맨 아래 행
        arr[R-1][j] = arr[R-1][j+1]
    for i in range(R-1, purifier, -1): # 맨 오른쪽 열
        arr[i][C-1] = arr[i-1][C-1]
    for j in range(C-1, 1, -1): # 공청기 아래 행.
        arr[purifier][j] = arr[purifier][j-1]
    arr[purifier][1] = 0 # 공청기 중 아래칸에서 나온 곳
    return arr


R, C, T = map(int, input().split()) # 격자 R/C. T초후.
arr = [list(map(int, input().split())) for _ in range(R)]
for _ in range(T):
    arr = spread()
    arr = purify()
ans = 2 # 공청기가 -1씩 2개 있음
ans += sum(map(sum, zip(*arr)))
print(ans)