'''
BFS 내에서 arr 복사본 생성
시작시 빈칸 개수를 먼저 저장. 0이 되면 종료.
BFS 탐색 내, 두가지 구분해야함.
- virus 번짐
- 시간 증가
'''

from itertools import combinations
from collections import deque

def BFS(case, empty):
    arr_now = [item[:] for item in arr] # arr 복사본 생성.
    queue = deque([])
    for i, j in case:
        arr_now[i][j] = 1 # virus
        queue.append((i, j))
    queue.append(1) # 시간 증가 flag
    cnt = 0 # 시간 초기화
    if not empty: # 빈공간 없음. 종료.
        return cnt
    while queue:
        v = queue.popleft()
        if not empty: # 더이상 빈자리가 없음. 루프 종료.
            break
        if v == 1: # 한턴 종료 flag.
            cnt += 1 # 시간 증가
            if queue: # 잔여 virus 있음
                queue.append(1) # 턴 종료 flag 다시 삽입
                continue
            else:
                break
        for d in range(4):
            x = v[0] + dx[d]
            y = v[1] + dy[d]
            if 0<=x<N and 0<=y<N:
                if not arr_now[x][y]: # 빈자리
                    arr_now[x][y] = 1 # virus화
                    queue.append((x, y))
                    empty -= 1 # 빈자리 감소
                elif arr_now[x][y] == 2: # virus
                    arr_now[x][y] = 1 #  벽 처리(이후 계산에서 제외)
                    queue.append((x, y))

    if not empty:
        return cnt+1
    else: # 불가능.
        return -1

N, M = map(int, input().split()) # 크기 N, 활성 바이러스 수 M
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
virus_candid = []
empty = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2: # virus 위치.
            virus_candid.append((i, j))
        if arr[i][j] == 0: # 빈칸. virus 가능성.
            empty += 1

cases = combinations(virus_candid, M) # 전체 virus 중 3개 조합 생성.
res = N**2 # 최대 가능 개수. arr 모든 곳에 virus.
for case in cases:
    cnt = BFS(case, empty)
    if cnt == -1: # 무시하고 다음 case 계산.
        continue
    if cnt < res:
        res = cnt
print(-1 if res==N**2 else res)