# https://velog.io/@youngjun0627/1014%EB%B2%88-%EC%BB%A8%EB%8B%9D
def check(x, cur, prev):
    cur |= (1 << x) # 앉은 자리 한개 추가
    if M == 1: # 전체 폭이 1일 경우
        return True # 무조건 가능
    if x == 0: # 첫 열
        if prev & (1 << x + 1) or cur & (1 << x + 1):
            return False
    if x == M - 1: # 마지막 열
        if prev & (1 << x - 1) or cur & (1 << x - 1):
            return False
    if 0 < x < M - 1: # 중간
        if prev & (1 << x + 1) or cur & (1 << x + 1) or prev & (1 << x - 1) or cur & (1 << x - 1): # 마
            return False

    return True


def DFS(y, row_case):
    global rows, DP
    if y == N: # 종료
        return 0
    if DP[y][row_case] != -1: # DP == visited + memory
        return DP[y][row_case]

    DP[y][row_case] = 0
    rows = []
    generate_row(y, 0, 0, row_case, rows) # y, x, cur, prev, rows

    for cur in rows:
        cnt = 0
        for i in range(M):
            if cur & (1 << i):
                cnt += 1

        DP[y][row_case] = max(DP[y][row_case], cnt + DFS(y + 1, cur))

    return DP[y][row_case]


def generate_row(y, x, cur, prev, rows):
    if x == M: #
        rows.append(cur)
        return

    if check(x, cur, prev) and arr[y][x] == '.': # ?? & 앉을 수 있는지
        generate_row(y, x + 1, cur | (1 << x), prev, rows) # 오른쪽으로 하나 증가
    generate_row(y, x + 1, cur, prev, rows) # 오른쪽으로 하나 증가


for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    rows = []
    DP = [[-1] * (1 << M) for _ in range(N)] # 한 행의 배치 case에 대한 bitmask
    print(DFS(0, 0))