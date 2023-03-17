'''
[설명]
바이러스는 활성 상태와 비활성 상태
가장 처음에 모든 바이러스는 비활성 상태
활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제, 1초
승원이는 연구소의 바이러스 M개를 활성 상태로 변경 -> combinatnion 조합 생성

N×N
연구소는 빈 칸, 벽, 바이러스
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변함

0은 빈 칸, 1은 벽, 2는 바이러스

[문제]
연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간
바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1
'''
'''
[알고리즘]
- virus_candid
    - 바이러스 놓을 수 있는 자리들
- empty
    - 빈칸 개수
- BFS
    - arr 복사본
    - virus 경우의 수 중 1에 대해 전부 queue 삽입 후 BFS
    - queue 삽입시, 시간 증가 flag를 함께 넣어야함
        - (x, y) or 1 in queue
    - if not empty (빈공간 없으면)
        - time + 1 종료
        - 예) 1턴 후 2턴 하다 중간에 끝나면, 2턴 종료

'''
'''
[구조]
- arr 저장
- virus_candid = virus 놓을 수 있는 자리 저장
- empty = 빈칸 개 
- for 전체 탐색:
    - if virus: 
        - virus_candid.append((i, j))
    - if 빈칸: 
        - empty += 1

- result = N**2 최대 가능 개수. arr 모든 곳에 virus.
- cases = virus 중 3개 조합 생성

- for cases:
    - time = BFS(case, empty)
    - if time == -1: 무시
    - if time < result:
        - result = time
- print(-1 if result==N**2 else result)

- BFS(case, empty):
    - arr_now = arr 복사본
    - for case:
        - arr_now[i][j] = virus 표시
        - queue.append((i, j))
    - queue.append(1) 시간 증가 flag
    - time = 0 시간 초기화
    - if 빈공간 없음: 
        - return time
    - while queue:
        - v = (x, y) or time flag(1)
        - if 빈공간 없음: break
        - if v == 1: 한턴 종료 flag.
            - time ++
            - if 잔여 virus 있음:
                - queue.append(1) # 턴 종료 flag 다시 삽입
                - continue
            - else:
                - break
        - for 4방:
            - if 범위내:
                - if 빈자리: 
                    - arr_now[x][y] = virus 화
                    - queue 추가
                    - empty --
                - elif virus:
                    - arr_now[x][y] = 벽 처리(이후 계산에서 제외)
                    - queue 추가

    - if 빈공간 없음:
        - return time+1
    - else: 불가능
        - return -1
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
    time = 0 # 시간 초기화
    if not empty: # 빈공간 없음. 종료.
        return time
    while queue:
        v = queue.popleft()
        if not empty: # 더이상 빈자리가 없음. 루프 종료.
            break
        if v == 1: # 한턴 종료 flag.
            time += 1 # 시간 증가
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
        return time+1
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
result = N**2 # 최대 가능 개수. arr 모든 곳에 virus.
for case in cases:
    time = BFS(case, empty)
    if time == -1: # 무시하고 다음 case 계산.
        continue
    if time < result:
        result = time
print(-1 if result==N**2 else result)