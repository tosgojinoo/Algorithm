'''
[설명]
3×3
인덱스는 1부터 시작
- 연산
    - 1초가 지날때마다 배열에 연산이 적용
    - R 연산
        - 배열 A의 모든 행에 대해서 정렬
        - 행의 개수 ≥ 열의 개수인 경우에 적용
    - C 연산 -> zip(*arr)
        - 배열 A의 모든 열에 대해서 정렬
        - 행의 개수 < 열의 개수인 경우에 적용
    - 한 행/열에 있는 수를 정렬
    - 각각의 수가 몇 번 나왔나
    - 수의 등장 횟수가 커지는 순 > 수가 커지는 순 정렬
    - 배열 A에 정렬된 결과를 다시 넣음. (수, 등장 횟수)
- 크기
    - 정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있음
    - R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변함 -> max_len. 보다 작으면 0으로 채움
    - C 연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변함
    - 행 또는 열의 크기가 커진 곳에는 0 채움
    - 수를 정렬할 때 0은 무시 -> [:arr[0]] slice
    - 행/열의 크기가 100을 넘어가는 경우 나머지 버림 [:100] slice

[문제]
A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간을 출력
100초가 지나도 A[r][c] = k가 되지 않으면 -1을 출력
'''
'''
[알고리즘]
- while True
    - 100 시간 초과 break
    - arr(r, c) == k 면 break
    - 행 or 열 연산 조건에 따라
        - arr 변환
        - calculate()
- 행/열 연산을 조건에 따라 방향만 바꿔서(zip(*arr)) 동일하게 calculate() 적용 
- calculate()
    - 행을 하나씩 루프
        - 행 내 (num, count(num)) 전부 계산, sort, 일렬로 붙이기
        - 최대 길이 갱신
    - 최대 길이 기준으로 부족분 0 채우기
    - 길이 100 넘으면 slice
'''
'''
[구조]
- arr 저장
- while True:
    - if 시간이 100 초과: break
    - if 범위 내 제시된 r/c 가 있고, arr(r, c) == k: break
    - if 행의 개수 >= 열의 개수. R연산 적용.
        - arr = calculate(arr)
    - else:
        - arr = calculate(list(zip(*arr))) # C연산 적용. transpose.
        - arr 원복
    - time ++
- calculate()
    - for row 하나씩 호출
        - (숫자, 개수)를 담을 배열 / 연산 후의 행(또는 열)을 담을 배열
        - for num in set(row): 
            - 0일 경우 무시
            - num_cnt.append((num, row.count(num))) # 각 숫자에 대해서 개수를 파악
        - sorted(num_cnt) 개수가 적은 순, 숫자가 작은 순. 오름차순.
        - 풀어서 리스트 하나로 합치기
        - row_list를 하나로 합치기. 전체 arr로.
        - 최대 길이 갱신
    - for row in new_arr 
        - 가장 긴 행(또는 열)의 크기에 맞춰 0 추가
        - 크기가 100이 넘어가면 슬라이싱
'''

import sys

input = sys.stdin.readline

def calculate(arr): # 배열A의 연산
    new_arr, length = [], 0 # 연산 후 반환할 행렬 / 최대 길이의 행(또는 열)
    for row in arr:
        num_cnt, new_row = [], [] # (숫자, 개수)를 담을 배열 / 연산 후의 행(또는 열)을 담을 배열
        for num in set(row): # 각 숫자에 대해서 개수를 파악
            if not num:
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
    if 0<= r-1 <len(arr) and 0<= c-1 <len(arr[0]) and arr[r-1][c-1] == k: # 범위 내 제시된 r/c 가 있고, arr(r, c) == k
        break
    if len(arr) >= len(arr[0]): # 행의 개수 >= 열의 개수. R연산 적용.
        arr = calculate(arr)
    else:
        arr = calculate(list(zip(*arr))) # C연산 적용. transpose.
        arr = list(zip(*arr))
    time += 1
print(time)