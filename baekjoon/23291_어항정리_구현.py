'''
[설명]
정육면체
한 변의 길이는 모두 1
어항은 N개
가장 처음에 어항은 일렬
어항에는 물고기가 한 마리 이상
칸에 적힌 값은 그 어항에 들어있는 물고기의 수

- 어항을 한 번 정리하는 과정
    - 먼저, 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다. -> 정리 조건
        - 만약, 그러한 어항이 여러개라면 물고기의 수가 최소인 어항 모두에 한 마리씩 넣는다.
- 어항을 쌓기
    - 먼저, 가장 왼쪽에 있는 어항을 그 어항의 오른쪽에 있는 어항의 위에 올려 놓음
    - 이제, 2개 이상 쌓여있는 어항을 모두 공중 부양시킨 다음, 전체를 시계방향으로 90도 회전
    - 이후 공중 부양시킨 어항을 바닥에 있는 어항의 위에 올려놓는다.
    - 바닥의 가장 왼쪽에 있는 어항 위에 공중 부양시킨 어항 중 가장 왼쪽에 있는 어항이 있어야 한다.
    - 공중 부양시킨 어항 중 가장 오른쪽에 있는 어항의 아래에 바닥에 있는 어항이 있을때까지 반복
- 어항에 있는 물고기의 수를 조절
    - 모든 인접한 두 어항에 대해서, 물고기 수의 차이 계산
    - 이 차이를 5로 나눈 몫을 d
    - d가 0보다 크면, 두 어항 중 물고기의 수가 많은 곳에 있는 물고기 d 마리를 적은 곳에 있는 곳으로 보낸다.
    - 이 과정은 모든 인접한 칸에 대해서 동시에 발생
- 어항을 바닥에 일렬로 놓기 -> 한줄 처리
    - 가장 왼쪽에 있는 어항부터,
        - 그리고 아래에 있는 어항부터 순서대로
- 공중 부양 작업 -> 반 접기
    - 가운데를 중심으로 왼쪽 N/2개를 공중 부양
    - 전체를 시계 방향으로 180도 회전 시킨 다음,
    - 오른쪽 N/2개의 위에 놓기
    - 두 번 반복
    - 바닥에 있는 어항의 수는 N/4개
- 여기서 다시 위에서 한 물고기 수 조절 작업 수행
- 바닥에 일렬로 놓는 작업 수행

[문제]
물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가 K 이하가 되려면 어항을 몇 번 정리해야 하는가
'''
'''
[알고리즘]
- 물고기 정리
    - 물고기 수가 최소인 어항 모두에 1개씩 추가
        - [l + (l == min_num) for l in arr] 
        - (l == min_num)으로, 조건 맞을 경우만 +1이 가능
    - 맨 왼쪽 어항 위로 쌓음
        - [[arr[0]]+[0]*(n-2), arr[1:]]
        - 맨 왼쪽만 분리 후 부족분을 0으로 채우고, 위로 붙이기

- roll_fishbowl_array()
    - 기준 idx 선정이 중요. 여기서는, 가장 윗칸 중 물고기가 있는 최대 idx+1(slice 고려).
    - 2개 이상 쌓은 어항
        - 부분 저장 공간 필요.
        - turn_N_upper 에 아래 행부터 저장.(idx 역순, transpose 쉽도록)
    - 90도 회전 -> transpose. zip(*arr). 
    - 이때 밑 바닥에 어항 개수가 충분할 경우 까지만 진행 
        - 중지 조건:
            - 맨 윗칸의 물고기 없는 칸(90도 회전 후 올라갈 공간) < arr 행 길이(90도 회전 후 맨 윗줄 길이)
    - return recursive
        - [*zip(*turn_N_upper)]]+[arr[-1]]: turn_N_upper를 90도 회전(transpose) + arr 잔여 마지막줄 붙임
        - [*row] + [0]*(len(arr[-1])-len(row)): 마지막줄 기준으로 호출된 row 길이의 부족분 만큼 [0]으로 채워 row 완성 
        - roll_fishbowl_array에 재귀 처리(조건에 맞지 않아 중지할 때 까지)
- control_fish_count()
    - 분배량 전체 확인 후 한번에 반영
    - tmp array에 따로 계산 후, 나중에 arr에 +/- 반영
- serialize_fishbowl_array()
    - 한줄로 만들기
    - 열 순 > 행 역순 > 물고기 있다면 > tmp 추가 > 마지막에 tmp return
- fold_fishbowl_array(arr, time):
    - 한줄 일 경우 -> 리스트로 한번 감싸서 차원 2차원으로 맞춰줘야함
    - 접기
        - 접었을 때 길이를 미리 저장
        - tmp 에 추가하는 방식으로 새로 구성
        - 절반을 180도 회전시켜 올리기
            - row 역순 > 절반 앞부분 slice > 역순 [::-1] > tmp 추가 > row 정순 > 절반 뒷부분 slice > tmp 추가
    - 2회 반복 -> 재귀 처리 후 time으로 중지
'''
'''
[구조]
- arr 물고기 정보 저장
- while turns:
    - min_num = min(arr)
    - arr = 물고기 수가 최소인 어항 모두에 1개씩 추가
    - arr = 맨 왼쪽 어항 위로 쌓음 + 추가된 행의 나머지는 0으로 채우기
    - arr = roll_fishbowl_array(arr) # 2개 이상 쌓인 부분 회전 후 붙임
    - control_fish_count() # 물고기 수 조절
    - arr = serialize_fishbowl_array() # 한줄 처리
    - arr = fold_fishbowl_array(arr) # 반 접기 2회
    - control_fish_count() # 물고기 수 조절
    - arr = serialize_fishbowl_array() # 한줄 처리
    - if 최대/최소 물고기수 차이 <= k: break
    - turns += 1
- print(turns)

- roll_fishbowl_array(arr):
    - max_idx = 가장 윗칸 중 물고기가 있는 최대 idx
    - turn_N_upper = 회전해 위에 붙일 부분 저장 공간
    - if [문제 조건] 맨 윗칸의 물고기 없는 칸(90도 회전 후 올라갈 공간) < arr 행 길이(90도 회전 후 맨 윗줄 길이): 
        return arr 중지 후 리턴
    - for 행 idx. 아래부터 역순:
        - turn_N_upper += 대상만큼 잘라서, 따로 저장
        - arr[i] = 나머지 저장

    # [*zip(*turn_N_upper)]]+[arr[-1]]: turn_N_upper를 90도 회전(transpose) + arr 잔여 마지막줄 붙임
    # [*row] + [0]*(len(arr[-1])-len(row)): 마지막줄 기준으로 호출된 row 길이의 부족분 만큼 [0]으로 채워 row 완성 
    # roll_fishbowl_array에 재귀 처리(조건에 맞지 않아 중지할 때 까지)
    - return roll_fishbowl_array([[*row]+[0]*(len(arr[-1])-len(row)) for row in [*zip(*turn_N_upper)]]+[arr[-1]])

- control_fish_count():
    - r, c = arr의 size 확인
    - T = arr 동일 크기의 빈 array 생성. 생선 분배량을 한번에 반영하기 위함.
    - for 전체 탐색:
        - for 4방향:
            - if 범위내, 물고기 있으면:
                - t = 차이를 5로 나눈 분배값 설정
                - if 분배값 양수일때:
                    - T[i][j] - t 원래에서 차감
                    - T[ni][nj] + t 옆으로 합산
    - for 전체 탐색:
        - arr에 분배량 T 반영

- serialize_fishbowl_array():
    - r, c = len(arr), len(arr[0])
    - tmp =[]
    - for 열 순:
        - for 행 역순:
            - if 물고기 있으면:
                - tmp에 추가
    

- fold_fishbowl_array(arr, time):
    - if 행 하나만 볼때 list type 아닐 경우(한 행 구성일 경우 처리):
        - arr = [arr]
    - n = 접었을 때 길이
    - if 3번째 반복인지: 
        - return arr
    - tmp = []
    - for row 역순:
        - tmp += 절반 앞부분의 역순
    - for row 정순:
        - tmp += 절반 뒷부분의 정순
    - return fold_fishbowl_array(tmp, time+1) 재귀
'''


def roll_fishbowl_array(arr):
    max_idx = max(idx+1 for idx in range(len(arr[0])) if arr[0][idx]) # 가장 윗칸 중 물고기가 있는 최대 idx
    turn_N_upper = []
    if len(arr[0])-max_idx < len(arr): # 조건: 맨 윗칸의 물고기 없는 칸(90도 회전 후 올라갈 공간) < arr 행 길이(90도 회전 후 맨 윗줄 길이)
        return arr # 중지 후 리턴
    for i in range(len(arr))[::-1]: # 행 idx. 아래부터 역순.
        turn_N_upper += [arr[i][:max_idx]] # 대상만큼 잘라서, 따로 저장
        arr[i] = arr[i][max_idx:] # 나머지 저장

    # [*zip(*turn_N_upper)]]+[arr[-1]]: turn_N_upper를 90도 회전(transpose) + arr 잔여 마지막줄 붙임
    # [*row] + [0]*(len(arr[-1])-len(row)): 마지막줄 기준으로 호출된 row 길이의 부족분 만큼 [0]으로 채워 row 완성
    # roll_fishbowl_array에 재귀 처리(조건에 맞지 않아 중지할 때 까지)
    return roll_fishbowl_array([[*row]+[0]*(len(arr[-1])-len(row)) for row in [*zip(*turn_N_upper)]]+[arr[-1]]) # recursive

def control_fish_count():
    r, c = len(arr), len(arr[0])
    T = [[0]*c for _ in range(r)] # arr 동일 크기의 빈 array 생성. 생선 분배량을 한번에 반영하기 위함.
    for i in range(r):
        for j in range(c):
            # 4방향
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < r and 0 <= nj < c and arr[ni][nj]: # 범위내, 물고기 있으면.
                    t = (arr[i][j]-arr[ni][nj])//5 # 차이를 5로 나눈 분배값 설정
                    if t > 0: # 분배값 양수일때
                        T[i][j] -= t # 원래에서 차감
                        T[ni][nj] += t # 옆으로 합산
    for i in range(r):
        for j in range(c):
            arr[i][j] += T[i][j] # 분배량 반영

def serialize_fishbowl_array():
    r, c = len(arr), len(arr[0])
    tmp = []
    for j in range(c):
        for i in range(r)[::-1]:
            if arr[i][j]:
                tmp.append(arr[i][j])
    return tmp

def fold_fishbowl_array(arr, time):
    if type(arr[0]) != list: # 한 행 구성일 경우 처리
        arr = [arr]
    n = len(arr[0])//2 # 접었을 때 길이
    if time == 2: # 2번 반복 끝남. 중지
        return arr
    tmp = []
    for row in arr[::-1]: # 역순
        tmp += [row[:n][::-1]] # 절반 앞부분의 역순
    for row in arr: # 정순
        tmp += [row[n:]] # 절반 뒷부분의 정순
    return fold_fishbowl_array(tmp, time+1)



n, k = map(int, input().split()) # 어항 수 N, 가장 많은 <> 적은 어항 물고기 수 차이 K 이하.
arr = [*map(int, input().split())] # 물고기 정보
turns = 1
while turns:
    min_num = min(arr)
    arr = [l + (l == min_num) for l in arr] # 물고기 수가 최소인 어항 모두에 1개씩 추가
    arr = [[arr[0]]+[0]*(n-2), arr[1:]] # 맨 왼쪽 어항 위로 쌓음 + 0으로 채우기
    arr = roll_fishbowl_array(arr) # 2개 이상 쌓은 어항을 때내어 90도 회전 후 위로 붙임. 이때 밑 바닥에 어항 개수가 충분할 경우 까지만 진행.
    control_fish_count()
    arr = serialize_fishbowl_array()
    arr = fold_fishbowl_array(arr, 0)
    control_fish_count()
    arr = serialize_fishbowl_array()
    if max(arr) - min(arr) <= k:
        break
    turns += 1
print(turns)