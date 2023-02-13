''' my idea
- arr: NxN
- 상어 idx: 1~M. M개 상어
- 1이 가장 강력함
- 자신의 칸에 냄새 뿌림
- 상하좌우 이동
- k 이동 후 냄새 소멸
- 이동 우선 순위
    - 상어별 우선순위 &
        - if 냄새 없는 칸
        - if 자신의 냄새가 있는 칸
- 모든 이동 후 한 칸에 여러마리 상어 있으면, 1번 제외 모두 밖으로 쫓겨남

0 1 2 3
↑ → ↓ ←
    상어1    상어2
0↑  2312    2130
1→  1302    ...
2↓  1023
3←  3120
- 상어별, 방향 idx별 우선순위 list 구성


DFS() -> x => 구현, 시뮬레이션 문제
- swap_shark_position()
- find_position()
- arr_update()

arr[r][c] = [idx, dir, scent]
arr에 상태값 지속 업데이트
visted X
'''
''' pypy3만 가능'''
import sys

input = sys.stdin.readline

def find(idx):
    for i in range(N):
        for j in range(N):
            if idx == arr_init[i][j]:
                return i, j

def init():
    for idx in range(1, M + 1):
        shark_pos[idx] = x, y = find(idx) # 상어_위치[idx] = 위치 (x,y). arr[i][j] == idx 인 i, j return.
        arr_info[x][y] = (idx, 0)

def clear(t):
    for i in range(N):
        for j in range(N):
            if arr_info[i][j][0] and arr_info[i][j][1] + K <= t:
                arr_info[i][j] = (0, 0)

def run(t):
    global sharks
    for shark_idx in sharks:
        x, y = shark_pos[shark_idx]
        nxt = (-1, -1)
        nxt_dir = 0
        for d in range(4):
            dx, dy = dxy[shark_pri[shark_idx - 1][shark_dir[shark_idx - 1] - 1][d]] # 1씩 쉬프트
            nx, ny = x + dx, y + dy
            if not (0<=nx<N) or not (0<=ny<N): # 범위 밖 무시
                continue
            if arr_info[nx][ny] == (0, 0): # 냄새 없으면 1순위
                nxt = (nx, ny)
                nxt_dir = d
                break
            if nxt[0] == -1 and arr_info[nx][ny][0] == shark_idx: # 본인 냄새
                nxt = (nx, ny)
                nxt_dir = d
        shark_dir[shark_idx - 1] = shark_pri[shark_idx - 1][shark_dir[shark_idx - 1] - 1][nxt_dir]
        shark_pos[shark_idx] = nxt
    dic = dict()
    del_idx = []
    for shark_idx in sharks:
        if shark_pos[shark_idx] not in dic.keys():
            dic[shark_pos[shark_idx]] = 1
            arr_info[shark_pos[shark_idx][0]][shark_pos[shark_idx][1]] = (shark_idx, t)
        else:
            del_idx.append(shark_idx)
    sharks = list(set(sharks) - set(del_idx))

def solve():
    init()
    for time in range(1, 1001): # 1000초간 진행
        run(time)
        clear(time)
        if len(sharks) == 1: # 1번 상어만 남았으면
            print(time) # 정상 출력
            return
    print(-1)


N, M, K = map(int, input().split())
arr_init = [list(map(int, input().split())) for _ in range(N)]
arr_info = [[(0, 0)] * N for _ in range(N)]

shark_dir = list(map(int, input().split()))
shark_pri = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)] # 방향 우선 순위.
sharks = list(range(1, M+1)) # 상어 idx만 관리
shark_pos = [(0, 0)] * (M+1)

dxy = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)] # 0, 아래, 위, 좌, 우

solve()