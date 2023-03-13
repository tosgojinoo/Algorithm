'''
[설명]
상어에는 1 이상 M 이하의 자연수, 모든 번호는 서로 다름
1의 번호를 가진 어른 상어는 가장 강력 -> 번호가 낮은 상어만 남음
N×N 격자, M개의 칸에 상어.

- 턴
    - 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌림 
    - 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동 -> run()
    - 자신의 냄새를 그 칸에 뿌림
    - 상어가 k번 이동하고 나면 냄새 사라짐 -> clear(), 냄새는 고정이고 상어는 이동하므로 둘을 분리 관리해야함.

- 이동 방향 결정
    - if 인접한 칸 중 아무 냄새가 없는 칸의 방향
    - elif 자신의 냄새가 있는 칸의 방향  
    - 다음 우선순위 -> 우선순위 memory 관리
        - 우선순위는 상어마다 다를 수 있음
        - 같은 상어라도 현재 상어가 보고 있는 방향에 따라 다를 수 있음 -> 상어 방향 관리
        - 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향

- 한 칸에 여러 마리 -> 상어 위치 관리
    - 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨남 -> 남아 있는 상어 idx 관리

- 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽 -> dxy 1부터. 우선순위 없음.

- 방향 우선순위
    - 위를 향할 때의 방향 우선순위
    - 아래를 향할 때의 우선순위
    - 왼쪽을 향할 때의 우선순위
    - 네 번째 줄은 오른쪽을 향할 때의 우선순위
    - 각 우선순위에는 1부터 4까지의 자연수가 한 번씩
    - 가장 먼저 나오는 방향이 최우선

맨 처음에는 각 상어마다 인접한 빈 칸이 존재
처음부터 이동을 못 하는 경우는 없음

[문제]
1번 상어만 격자에 남게 되기까지 걸리는 시간 -> 경우의 수가 없어 DFS/BFS x. 구현.
1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1
'''
'''
[알고리즘]
- arr
    - (상어 위치, 방향)은 변하기 때문에, 분리 관리
    - (상어 idx, 냄새 유효기간)은 고정적이므로, arr에 저장
- 상어 관련 memory
    - shark_smell = (shark_idx, time) 저장. arr과 동일 크기. 상어 냄새 사라짐 확인용.
    - shark_pos = 상어 위치 저장
    - shark_dir = 상어 방향 저장
    - shark_pri = 상어별 방향 우선 순위 (참조용)
    - sharks = 남은 상어 idx 관리 <- 상어 idx에 따라 밀어내기가 가능하므로, arr에 남아있는 상어 idx 총량이 변함
- 이동
    - 일단, 상어별 우선순위 고려해 전부 이동
    - 상어 위치 중복 확인
    - 상어 idx 우선순위에 따라 한번에 정리
'''
'''
[구조]
- arr_init = 전체 맵 + x번 상어 위치
- shark_smell = (shark_idx, time) 저장
- shark_pos = 상어 위치 저장
- shark_dir = 상어 방향 저장
- shark_pri = 상어별 방향 우선 순위
- sharks = 남은 상어 idx 관리

- dxy = 0, 상, 하, 좌, 우
- init() arr_init -> shark_smell (shark_idx, time) 으로 변환, shark_pos 구성.
- solve()

- init():
    - for 상어 수 만큼:
        - shark_pos[idx] = arr에서 idx 상어의 위치 찾아 저장
        - shark_smell[x][y] = (상어 idx, 냄새 유효기간) 

- find(idx):
    - for 전체 탐색
        - if idx를 arr에서 찾으면:
            - return i, j

- solve():
    - for 1000초간 진행:
        - run(time)
        - clear(time)
        - if 1번 상어만 남았으면:  
            - print(time) 
            - return
    - 비정상 종료 print(-1)

- clear(time):
    - for 전체 탐색:
        - if shark_smell이 있고, (shark_smell 기록시간 + 지속시간 K <= 현시간):
            - shark_smell = (0, 0) 처리

- run(time):
    - for shark_idx 하나씩 확인:
        - 상어 위치 확인
        - for 4방향:
            - 우선순위 고려한 dxy 계산 및 추가
            - if 범위 밖: 무시
            - if 냄새 없으면 (1순위): 
                - nxt_loc, nxt_dir 저장
                - break
            - if nxt_loc 입력이 아직이고, 본인 냄새:
                - nxt_loc, nxt_dir 저장
        - shark_dir = 우선순위 고려한 다음 방향
        - shark_pos = 다음 위치
    - 위치 중복 확인용 dict 생성. check_pos 
    - 삭제할 상어 idx 저장. del_idx
    - for shark_idx 하나씩 확인:
        - if check_pos.keys() 에 위치 없으면:
            - check_pos에 추가
            - shark_smell = (shark_idx, time) 기록
        - else 위치 중복:
            - 삭제 대상 추가
    - 상어 idx 갱신

'''

import sys

input = sys.stdin.readline


def init():
    for idx in range(1, M + 1):
        shark_pos[idx] = x, y = find(idx) # 상어_위치[idx] = 위치 (x,y). arr[i][j] == idx 인 i, j return.
        shark_smell[x][y] = (idx, 0)

def find(idx):
    for i in range(N):
        for j in range(N):
            if idx == arr_init[i][j]:
                return i, j

def clear(time):
    for i in range(N):
        for j in range(N):
            if shark_smell[i][j][0] and shark_smell[i][j][1] + K <= time:
                shark_smell[i][j] = (0, 0)

def run(time):
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
            if shark_smell[nx][ny] == (0, 0): # 냄새 없으면 1순위
                nxt = (nx, ny)
                nxt_dir = d
                break
            if nxt[0] == -1 and shark_smell[nx][ny][0] == shark_idx: # 본인 냄새
                nxt = (nx, ny)
                nxt_dir = d
        shark_dir[shark_idx - 1] = shark_pri[shark_idx - 1][shark_dir[shark_idx - 1] - 1][nxt_dir]
        shark_pos[shark_idx] = nxt
    check_pos = dict()
    del_idx = []
    for shark_idx in sharks:
        if shark_pos[shark_idx] not in check_pos.keys():
            check_pos[shark_pos[shark_idx]] = 1
            shark_smell[shark_pos[shark_idx][0]][shark_pos[shark_idx][1]] = (shark_idx, time)
        else:
            del_idx.append(shark_idx)
    sharks = list(set(sharks) - set(del_idx))

def solve():
    for time in range(1, 1001): # 1000초간 진행
        run(time)
        clear(time)
        if len(sharks) == 1: # 1번 상어만 남았으면
            print(time) # 정상 출력
            return
    print(-1)


N, M, K = map(int, input().split()) # 격자 N, 상어수 M, 냄새 지속 시간 K
arr_init = [list(map(int, input().split())) for _ in range(N)] # x번 상어 위치
shark_smell = [[(0, 0)] * N for _ in range(N)] # (shark_idx, time) 저장. arr과 동일 크기.

shark_dir = list(map(int, input().split())) # 상어 방향 관리
shark_pri = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)] # 방향 우선 순위.
sharks = list(range(1, M+1)) # 남은 상어 idx 관리
shark_pos = [(0, 0)] * (M+1)

dxy = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)] # 0, 상, 하, 좌, 우
init()
solve()