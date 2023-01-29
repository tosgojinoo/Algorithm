# memory로 푸는 방식
# visited 대비 메모리, 시간 모두 2.5배 정도 더 소요
# 동적으로 구성하기 때문인 것으로 생각됨
from collections import deque

def BFS(by,bx,ry,rx):
    global memory
    q = deque([(by,bx,ry,rx, 1)])
    while q:
        by, bx, ry, rx, cnt = q.popleft()
        # 종료조건 1
        if cnt > 10: break
        for dy, dx in moves:
            # 한번에 움직일 수 있는 최대로 움직임
            nry, nrx, r_move_cnt = move_result(ry, rx, dy, dx)
            nby, nbx, b_move_cnt = move_result(by, bx, dy, dx)
            # B 구슬이 구멍에 빠지지 않은 경우만 확인
            if arr[nby][nbx] != 'O':
                # 종료조건 2
                # R 구슬 빠지면 성공
                if arr[nry][nrx] == 'O':
                    print(cnt)
                    return
                # R 공과 B 공이 만날 경우
                if nby == nry and nbx == nrx:
                    # *** 움직인 거리가 더 긴 것을 한칸 전으로 옮김
                    if r_move_cnt > b_move_cnt:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy
                # 방문 안했을 경우
                if (nby, nbx, nry, nrx) not in memory:
                    memory.add((nby, nbx, nry, nrx))
                    q.append((nby,nbx,nry,nrx, cnt+1))

    # 종료조건 3
    print(-1)

def move_result(y, x, dy, dx):
    move_cnt = 0
    # 가능한 곳까지 이동
    while arr[y+dy][x+dx]!="#" and arr[y][x]!='O':
        y+=dy
        x+=dx
        move_cnt+=1
    return y, x, move_cnt

N, M = map(int, input().split()) # 세로 크기는 N, 가로 크기는 M
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ry, rx = i, j
        if arr[i][j] == 'B':
            by, bx = i, j

moves = [(1,0), (-1,0), (0,1), (0,-1)]
memory = set()
memory.add((by, bx, ry, rx))
BFS(by,bx,ry,rx)
