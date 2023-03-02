import sys

input = sys.stdin.readline

def calculate(arr): # 배열A의 연산
    new_arr, length = [], 0 # 연산 후 반환할 행렬 / 최대 길이의 행(또는 열)
    for row in arr:
        num_cnt, new_row = [], [] # (숫자, 개수)를 담을 배열 / 연산 후의 행(또는 열)을 담을 배열
        for num in set(row): # 각 숫자에 대해서 개수를 파악
            if num == 0:
                continue # 0일 경우 continue
            cnt = row.count(num)
            num_cnt.append((num, cnt))
        num_cnt = sorted(num_cnt, key=lambda x:[x[1], x[0]]) # 정렬. # 개수가 적은 순, 숫자가 작은 순. 오름차순.
        for num, cnt in num_cnt:
            new_row += [num, cnt] # 풀어서 합치기
        new_arr.append(new_row)
        length = max(length, len(new_row)) # 최대 길이 갱신

    for row in new_arr: # 가장 긴 행(또는 열)의 크기에 맞춰 0 추가
        row += [0] * (length - len(row))
        if len(row) > 100:
            row = row[:100] # 크기가 100이 넘어가면 슬라이싱

    return new_arr


r, c, k = map(int, input().split()) # 목표 arr[r][c] == k
arr = [list(map(int, input().split())) for _ in range(3)] # 3행 고정
time = 0
while True:
    if time > 100: # 시간이 100 초과
        time = -1
        break
    if 0 <= r-1 < len(arr) and 0 <= c-1 < len(arr[0]) and arr[r-1][c-1] == k: # 범위 내 and arr(r, c) == k
        break
    if len(arr) >= len(arr[0]): # 행의 개수 >= 열의 개수. R연산 적용.
        arr = calculate(arr)
    else:
        arr = calculate(list(zip(*arr))) # C연산 적용. transpose.
        arr = list(zip(*arr))
    time += 1
print(time)