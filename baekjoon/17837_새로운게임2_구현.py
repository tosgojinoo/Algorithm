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
            horse[idx][2] = convert_direction(d) # 방향 반대
            d = horse[idx][2]
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


N, K = map(int, input().split())
arr = [[-1] + list(map(int, input().split())) if i > 0 else [-1]*(N + 1) for i in range(N + 1)] # idx 1부터 시작. -1로 맨 윗행, 좌측행 padding
horse = [list(map(int, input().split())) for _ in range(K)] # 말 정보. [행, 열의 번호, 이동 방향]
stack = [[[] for _ in range(N+1)] for _ in range(N+1)] # 누적 말 개수 저장.

direction = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)] # 방향 idx 1부터 시작. 우, 좌, 상, 하.
for idx, [ir, ic, _] in enumerate(horse):
    stack[ir][ic].append(idx)

time = 1
while time < 1001:
    if simulate():
        break
    time += 1
if time == 1001:
    print(-1)
else:
    print(time)
