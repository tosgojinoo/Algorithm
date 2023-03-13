'''
[설명]
N×N
파이어볼 M개

가장 처음에 파이어볼은 각자 위치에서 이동 대기
i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si
(r, c)는 r행 c열

격자의 행과 열은 1번부터 N번
1번 행은 N번과 연결 -> 맵 연결
1번 열은 N번 열과 연결

파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향 -> dxy 조건
7	0	1
6	 	2
5	4	3

- 명령
    - 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동
        - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있음
    - 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸
        - 같은 칸에 있는 파이어볼은 모두 하나로 합
        - 파이어볼은 4개의 파이어볼로 나눔
        - 나누어진 파이어볼의 질량, 속력, 방향
            - 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋
            - 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
            - 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수
                - 방향은 0, 2, 4, 6
                - 그렇지 않으면 1, 3, 5, 7
        -  질량이 0인 파이어볼은 소멸

둘째 줄부터 M개의 줄에 파이어볼의 정보가 한 줄에 하나씩 주어진다.
파이어볼의 정보는 다섯 정수 ri, ci, mi, si, di로 이루어져 있다.

서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.

[문제]
이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합
'''
'''
[알고리즘]
- 가장자리 맵 연결
    - 첫 행은 마지막 행과, 첫 열은 마지막 열과 연결
    - 맵 길이로 나 나머지 만큼만 이동
    - (r + dr[d] * s) % N, (c + dc[d] * s) % N
- memory
    - fire_pose: 파이어볼 정보를 저장 (r, c, m, s, d) 
    - updated: 파이어볼 이동 결과 위치 (nr, nc)
- arr
    - 이동 결과 위치에 파이어볼 정보 기록
    - arr(r,c) = (m, s, d)
'''
'''
[구조]
- dxy = 8방향. 12시 부터 시계방향
- arr = N x N. init list()

- fire_pos = [] 파이어볼 정보 저장
- for 파이어볼 정보 개수: 
    - fire_pos.append((map(int, input().split()))) # 파이어볼 정보 저장. 위치r, 위치c, 질량m, 속력s, 방향d

- for 이동 명령수:
    - move_fires()
    
- for fire_pos:
    answer += m
- print(answer)

- move_fires(): # 한번의 이동
    - updated = set() 업데이트 된 지점 저장
    - while fire_pos:
        - nr, nc = 맵 연결 방식. 나머지 만큼만 이동
        - arr[nr][nc] 에 (m, s, d) 추가
        - updated 에 (nr, nc) 추가
    - update_fires(updated)

-  update_fires(updated):
    for updated:
        - cmd_cnt = arr(x,y) 내 명령 개수
        - if 명령 1개:
            - fire_pos 에 다시 저장 (x, y, m, s, d)
        - elif 명령 2개 이상 (단일칸 파이어볼 중복):
            - sum_m, sum_s, d_cnt = 초기화
            - for arr[x][y]:
                - sum_m, sum_s 누적 질량, 속력
                - if not (d % 2): # 짝수 방향만 d_cnt 
                    d_cnt += 1
            - arr[x][y] = [] 초기화
            - sum_m //= 5
            - sum_s //= cmd_cnt
            - if sum_m 질량이 0: 무시
            # 짝수 방향 d_cnt = (0 : 전부 홀수 방향 | 전체 개수와 동일: 전부 짝수 방향) -> 짝수 방향으로 퍼지기
            # 아니면 홀수 방향으로 퍼지기 
            - dirs = (0, 2, 4, 6) if d_cnt in (0, cmd_cnt) else (1, 3, 5, 7)
            - for dirs:
                - fire_pos 에 추가 (x, y, sum_m, sum_s, d)


'''

def move_fires():
    updated = set()
    while fire_pos:
        r, c, m, s, d = fire_pos.pop()
        nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
        arr[nr][nc].append((m, s, d))
        updated.add((nr, nc))
    update_fires(updated)

def update_fires(updated):
    for x, y in updated:
        cmd_cnt = len(arr[x][y])
        if cmd_cnt == 1:
            m, s, d = arr[x][y].pop()
            fire_pos.append((x, y, m, s, d))
        elif cmd_cnt >= 2:
            sum_m, sum_s, d_cnt = 0, 0, 0
            for m, s, d in arr[x][y]:
                sum_m += m
                sum_s += s
                if not (d % 2):
                    d_cnt += 1
            arr[x][y] = []
            sum_m //= 5
            sum_s //= cmd_cnt
            if not sum_m:
                continue
            dirs = (0, 2, 4, 6) if d_cnt in (0, cmd_cnt) else (1, 3, 5, 7)
            for d in dirs:
                fire_pos.append((x, y, sum_m, sum_s, d))


dr = [-1, -1, 0, 1, 1, 1, 0, -1] # 8방향. 위 부터 시계방향.
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, F, K = map(int, input().split()) # size, 정보 개수, 이동 명령수
arr = [[[] for _ in range(N)] for _ in range(N)]

fire_pos = []
for _ in range(F):
    fire_pos.append((map(int, input().split())))

for _ in range(K):
    move_fires()
answer = 0
for _, _, m, _, _ in fire_pos:
    answer += m
print(answer)