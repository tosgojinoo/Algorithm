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
    for i in range(K):
        r, c, d = horse[i] # [행, 열의 번호, 이동 방향]
        nr, nc = r + direction[d][0], c + direction[d][1]
        if not 0 < nr <= N or not 0 < nc <= N or arr[nr][nc] == 2:
            horse[i][2] = convert_direction(d)
            d = horse[i][2]
            nr, nc = r + direction[d][0], c + direction[d][1]
            if not 0 < nr <= N or not 0 < nc <= N or arr[nr][nc] == 2:
                continue
        hi = stack[r][c].index(i)
        h = stack[r][c][hi:]
        stack[r][c] = stack[r][c][:hi]
        if arr[nr][nc] == 1:
            h.reverse()
        for hh in h:
            horse[hh] = [nr, nc, horse[hh][2]]
        stack[nr][nc].extend(h)
        if len(stack[nr][nc]) >= 4:
            return True
    return False


N, K = map(int, input().split())
arr = [[-1] + list(map(int, input().split())) if i > 0 else [-1]*(N + 1) for i in range(N + 1)] # -1로 맨 윗행 padding
horse = [list(map(int, input().split())) for _ in range(K)] # 말 정보. [행, 열의 번호, 이동 방향]
stack = [[[] for _ in range(N+1)] for _ in range(N+1)] # 말 정보 재배열.

direction = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)] # 방향 idx 1부터 시작
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
