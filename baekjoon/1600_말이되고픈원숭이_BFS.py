# import sys
from collections import deque

# input = sys.stdin.readline

def BFS():
    queue = deque()
    queue.append((0, 0, 0, K))
    DP[0][0] = 0

    while queue:
        x, y, cnt, k = queue.popleft()

        if x == H - 1 and y == W - 1: # 종료점 도착
            return cnt

        if k >= 1: # 말처럼 이동 횟수 잔여분
            for d in range(8):
                nx = x + horse_dx[d]
                ny = y + horse_dy[d]

                if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] != 1: # 범위 내, 장애물 아님.
                    if DP[nx][ny] < k - 1: # 말처럼 이동 횟수 잔여분이 이전 보다 많을 경우(유리한 상황)
                        DP[nx][ny] = k - 1
                        queue.append((nx, ny, cnt + 1, k - 1))

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] != 1: # 범위 내, 장애물 아님.
                if DP[nx][ny] < k:
                    DP[nx][ny] = k
                    queue.append((nx, ny, cnt + 1, k))

    return -1


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
DP = [[-1] * W for _ in range(H)]

horse_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dy = [1, 2, 2, 1, -1, -2, -2, -1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(BFS())