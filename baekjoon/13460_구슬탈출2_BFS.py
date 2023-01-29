# 빨간 구슬을 구멍을 통해 빼내는 게임
# 파란 구슬이 구멍에 들어가면 안 된다. 구슬이 동시에 구멍에 빠져도 실패. 동시에 같은 칸에 있을 수 없다.
# 4방향
# 최소 몇 번

# 특징:
# 0) 이동은 1칸 단위가 아님
# => 벽 or 구멍 만날때 까지 계속 이동
# 1) 'R', 'B'는 만날 수 없다.
# => 이동 후 동일칸 불가 => 분리 및 수정 과정 필요
# 2) 다음 이동 위치에 벽이 있을 경우, 제자리 유지

# checklist
# DP? x 점화식 아님
# heap? x 우선 순위에 의해 순서 줄일 필요 없음
# DFS?
# BFS? O
# *** visited x => 반복 방문 가능 => 틀림!! => 위치가 아닌 case에 대한 visited 함수 필요. 4차원(bx, by, rx, ry) 고려
# memory o 이전과 동일한 구슬 위치는 제외 => memory 보다 visited로 풀이

# 종료 조건
# 1) 기울인 횟수 10 초과
# 2) 기울인 횟수 10 이하, 빨간공 구멍에 들어감
# 3) 아닐 경우 return -1

from collections import deque

def BFS(by,bx,ry,rx):
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
                if not visited[nby][nbx][nry][nrx]:
                    visited[nby][nbx][nry][nrx] = True
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
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[by][bx][ry][rx] = True
BFS(by,bx,ry,rx)
