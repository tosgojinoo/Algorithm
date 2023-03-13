'''
[설명]
N×N
행과 열의 번호는 1부터 시작 -> arr의 좌/상단 -1로 padding
말의 개수는 K
하나의 말 위에 다른 말을 올릴 수 있음
체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나 (0은 흰색, 1은 빨간색, 2는 파란색)
말 K개를 놓고 시작
말은 1번부터 K번까지 번호
이동 방향은 위, 아래, 왼쪽, 오른쪽 4가지 중 하나 (1 →, 2 ←, 3 ↑, 4 ↓) -> dxy
턴 한 번은 1번 말부터 K번 말까지 순서대로 이동
한 말이 이동할 때 위에 올려져 있는 말도 함께 이동
턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.

- 말의 이동
    - A번 말이 이동하려는 칸이
        - 흰색인 경우
            - 그 칸으로 이동
            - 이동하려는 칸에 말이 이미 있는 경우
                - 가장 위에 A번 말을 올려 높음
                - A번 말의 위에 다른 말이 있는 경우
                    - A번 말과 위에 있는 모든 말이 이동
        - 빨간색인 경우
            - 이동한 후
            - A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꿈
            - 이동하려는 칸에 말이 이미 있는 경우
                - 가장 위에 A번 말을 올려 놓음
                - A번 말의 위에 다른 말이 있는 경우
                    - A번 말과 위에 있는 모든 말이 이동
        - 파란색인 경우 & 체스판을 벗어나는 경우
            - A번 말의 이동 방향 반대
            - 한 칸 이동
            - 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우
                - 이동하지 않고 가만히

다음 K개의 줄에 말의 정보가 1번 말부터 순서대로 주어진다.
말의 정보는 세 개의 정수로 이루어져 있고, 순서대로
같은 칸에 말이 두 개 이상 있는 경우는 입력으로 주어지지 않는다.

[문제]
게임이 종료되는 턴의 번호
1000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1
'''
'''
[알고리즘]
- stack
    - arr 내 위치 뿐만 아니라, 한 칸 내 말의 누적 상태에서 위치도 관리 필요.
    - arr 동일 사이즈 준비, 누적 현황 기록.
- 말 이동
    - 이동하려는 위치에 말이 있을 경우 얹기
        - stack[r][c] 확인 > 말 stack 내 기준 말 idx 확인 > slice > 이동 > stack.extend(stack_over)
    - 빨간색일 경우
        - stack_over.reverse() 순서 변경
'''
'''
[구조]
- 크기 N, 말의 개수 K
- arr 저장
    - idx 1부터 시작
    - -1로 맨 윗행, 좌측행 padding
- horse = 말 정보. (행, 열, 이동 방향)
- stack
    - 누적 말 개수
    - arr과 동일 사이즈
    - 각 위치에 horse 정보 기록(초기값)
- direction: 방향 idx 1부터 시작. 0, 우, 좌, 상, 하.

- while 1001 미만 횟수 동안:
    - if simulate(): 종료
    
- simulate():
    - for horse_idx:
        - 말의 행, 열의 번호, 이동 방향 확인
        - 이동
        - if 범위 밖(유효 arr 범위는 1~N) or 파란색:
            - 말 방향 반대 convert_direction(d)
            - 반대로 이동
            - if 범위 밖(유효 arr 범위는 1~N) or 파란색: 무시
        - 단일칸 내 누적 말 중 자신의 위치 확인 stack[r][c].index(idx) 
        - 자신을 포함한 이후의 말들 따로 저장  
        - 자신을 포함한 위의 말을 제외하고, 나머지를 현 위치에 남김.
        - if 빨간색: 
            - 순서 변경 stack_over.reverse()
        - for 옮길 말들의 idx:
            - 말 정보 갱신 horse[s_o_idx]
        - 옮겨질 자리에 말을 얹힘 stack[nr][nc].extend(stack_over) 
        - if 누적 말 개수 4개 이상:
            - 정상 종료 return True
    - 비정상 종료 return False
    
- convert_direction(d):
    - 상하 끼리 전환
    - 좌우 끼리 전환
'''

def convert_direction(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    else:
        return 3


def simulate():
    global stack, horse
    for idx in range(K):
        r, c, d = horse[idx] # [행, 열의 번호, 이동 방향]
        nr, nc = r + direction[d][0], c + direction[d][1] # 이동
        if not 0 < nr <= N or not 0 < nc <= N or arr[nr][nc] == 2: # arr idx가 1부터 시작. 유효 arr 범위는 1~N. 파란색
            horse[idx][2] = d = convert_direction(d) # 방향 반대
            nr, nc = r + direction[d][0], c + direction[d][1] # 반대로 이동
            if not 0 < nr <= N or not 0 < nc <= N or arr[nr][nc] == 2: # 방향 바꿨는데, 파란색이면 정지
                continue
        s_idx = stack[r][c].index(idx) # 누적 말 중 자신의 위치
        stack_over = stack[r][c][s_idx:] # 자신을 포함한 이후의 말들
        stack[r][c] = stack[r][c][:s_idx] # 자신을 포함한 위의 말을 제외하고 남김
        if arr[nr][nc] == 1: # 빨간색
            stack_over.reverse() # 순서 변경 후
        for s_o_idx in stack_over: # 이동
            horse[s_o_idx] = [nr, nc, horse[s_o_idx][2]] # 말 정보 갱신
        stack[nr][nc].extend(stack_over) # 옮겨질 자리에 말을 얹힘
        if len(stack[nr][nc]) >= 4: # 누적 말 개수 4개 이상 종료
            return True
    return False


N, K = map(int, input().split()) # 체스판의 크기 N, 말의 개수 K
arr = [[-1] + list(map(int, input().split())) if i > 0 else [-1]*(N + 1) for i in range(N + 1)] # idx 1부터 시작. -1로 맨 윗행, 좌측행 padding
horse = [list(map(int, input().split())) for _ in range(K)] # 말 정보. (행, 열, 이동 방향)
stack = [[[] for _ in range(N+1)] for _ in range(N+1)] # 누적 말 개수 저장. arr과 동일 사이즈
for idx, [ir, ic, _] in enumerate(horse):
    stack[ir][ic].append(idx)
direction = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)] # 방향 idx 1부터 시작. 우, 좌, 상, 하.

time = 1
while time < 1001:
    if simulate():
        break
    time += 1
if time == 1001:
    print(-1)
else:
    print(time)
