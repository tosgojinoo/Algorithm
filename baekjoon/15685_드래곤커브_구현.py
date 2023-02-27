'''
0세대 : 0
1세대 : 0 1
2세대 : 0 1 2 1
3세대 : 0 1 2 1 2 3 2 1
4세대 : 0 1 2 1 2 3 2 1 2 3 0 3 2 3 2 1
'''
import sys

input = sys.stdin.readline

n = int(input())

dx = [1, 0, -1, 0] # 우, 상, 좌, 하
dy = [0, -1, 0, 1]

# 드래곤 커브들이 모일 배열 1이면 드래곤 커브의 일부
arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split()) # x, y: 드래곤 커브 시작점, d: 시작 방향, g: 세대
    arr[x][y] = 1

    move = [d]
    # g 세대 만큼 반복
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-(i + 1)] + 1) % 4) # 다음 세대 방향 생성 로직. 이전 세대의 정보를 뒤집어 거기에 +1. 4면 다시 처음인 0으로 변경.
        move.extend(tmp)

    # 드래곤 커브에 해당하는 좌표 arr에 추가
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        arr[nx][ny] = 1
        x, y = nx, ny

# 모든 꼭짓점이 드래곤 커브의 일부인 정사각형 개수 구하기
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]: # 4꼭지점 확인
            ans += 1

print(ans)