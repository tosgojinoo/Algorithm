def check(lst):
    buffer = 1
    for idx, height in enumerate(lst):
        if idx == 0:
            continue
        if height == lst[idx-1]: # 바로 이전과 높이 동일
            buffer += 1
        elif height == lst[idx-1] + 1: # 이전 보다 높이 +1
            if buffer < L:
                return 0
            buffer = 1 # 경사로 놓고, 초기화
        elif height == lst[idx-1] - 1: # 이전 대비 높이 -1
            if buffer < 0: # 이 조건에 진입했을 땐, 이미 debt이 없는 상태여야함. 있다는 것은, 경사로 밑면이 충분히 확보되지 않았다는 것.
                return 0
            buffer = -L + 1 # 경사로 길이 만큼 debt
        else: # 높이차가 +/-1 초과하면, 아웃
            return 0

    if buffer < 0: # 잔여 debt 이 있을 경우, 아웃
        return 0

    return 1

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

row_sum = 0
for lst in arr:
    row_sum += check(lst)

col_sum = 0
for lst in zip(*arr):
    col_sum += check(lst)
print(row_sum + col_sum)