'''
[설명]
N×N
N은 항상 홀수
(r, c)는 격자의 r행 c열
격자의 가장 왼쪽 윗 칸은 (1, 1)
가장 오른쪽 아랫 칸은 (N, N)
마법사 상어는 ((N+1)/2, (N+1)/2)

일부 칸과 칸 사이에는 벽
실선은 벽이고, 점선은 벽 아님
칸에 적혀있는 수는 칸의 번호

가장 처음에 상어가 있는 칸을 제외한 나머지 칸에는 구슬이 하나 들어갈 수 있다.
구슬은 1번 구슬, 2번 구슬, 3번 구슬
같은 번호를 가진 구슬이 번호가 연속하는 칸에 있으면, 그 구슬을 연속하는 구슬

- 블리자드 마법
    - 방향 di와 거리 si
    - 4가지 방향 ↑, ↓, ←, →가 있고, 정수 1, 2, 3, 4
    - di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴 -> di 방향 직선 위만 파괴
    - 구슬이 파괴되면 그 칸은 구슬이 들어있지 않은 빈 칸
    - 벽은 파괴 x
- 구슬 이동 -> shell 처리보다, 1D 처리가 원활하므로 추가 구성 -> cur_list
    - 만약 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸
        - A에 있는 구슬은 그 빈 칸으로 이동
    - 더이상 구슬이 이동하지 않을 때까지 반복
    - 구슬 파괴 > 빈 칸 > 구슬 이동
- 구슬 폭발
    - 4개 이상 연속하는 구슬
    - 빈 칸 > 구슬 이동 > 구슬 폭발
    - 이 과정은 더 이상 폭발하는 구슬이 없을때까지 반복
- 구슬 변화
    - 연속하는 구슬은 하나의 그룹
    - 하나의 그룹은 두 개의 구슬 A와 B로 변함
    - 구슬 A의 번호는 그룹에 들어있는 구슬의 개수
    - B는 그룹을 이루고 있는 구슬의 번호
    - 구슬은 다시 그룹의 순서대로 1번 칸부터 차례대로 A, B의 순서로 칸에 들어감
    - 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 구슬 제거

[문제]
1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수) 출력
'''
'''
[알고리즘]
- memory
    - direction_cnt
        - shell 회전
            - 격자 중심에서부터 shell 회전시, 
            - 방향 전환 전까지의 연속 칸수(직선길이)는, 2개씩 묶어서 증가 계산
            - [i//2 for i in range(2, N*2)]
            - 예) [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6] # 좌,하, 우,상, 좌,하, 우,상, ...
        - shell용 반시계 방향 ←, ↓, →, ↑
    - cur_list
        - 빈 자리가 생기고 다시 채우는 과정은 arr 상태에서 처리하기 어려움
        - 1D로 변환 구성해 활용
        - for direction_cnt
            - for range(dc) 
                - dxy[d] 만큼 이동하며 arr값 -> cur_list 
            - d 방향 전환 (d+1)%4
    - icebreak_idx_in_cur
        - 마법에 의한 구슬 폭발의 쉬운 계산을 위해 1D cur_list 상태에서 폭발 적용하는 idx를 미리 계산
        - 마법 적용 범위는 중심점에서 4방 중 하나 직선상 적용
        - shell개수 = N//2. 4방 번걸아가며 계산.
        - (북 -> 서), (서 -> 남) 전환시 +1씩 증분 
            - if i%4 in (0, 3): plus ++
        #      [1,| 3, 5, 7, 10, 14, 18, 22, 27, 33, 39, 45]
        # plus: 2,| 2, 2, 3,  4,  4,  4,  5,  6,  6,  6,  -
        # i   : 1,| 2, 3, 4,  5,  6,  7,  8,  9, 10, 11,  -
        # init    |
    - marvel_cnt
        - 구슬 번호에 따라 폭발 개수 구분 필요
        - idx == 구슬 번호 매핑 관리
- dxy
    - shell 용: ←, ↓, →, ↑
    - 문제용   : _, ↑, ↓, ←, → (idx 1부터 시작)
    - 매핑 테이블 d_map = [0, 3, 1, 0, 2]
    - dxy[d_map[idx]]
- move_marvel()
    - 파괴된 구슬(0) 제거하고, 앞으로 구슬 옮기고, 뒷부분 0으로 채우려면
    - while 0 in cur_list:
        - cur_list.remove(0)
    - [0] + cur_list + [0] * (N*N - len(cur_list) - 1)
- explosion, change_list
    - 두 함수 모두 start/end idx를 이동시켜가며 구간 형성 후 계산
    - 조건에 부합할때 까지 end idx 이동 후 계산
    - 계산 끝나면 start/end idx 초기화
        - start <- end
        - end <- start+1
'''
'''
[구조]
- arr = 격자에 들어 있는 구슬 정보. 없으면 0. 상어 있으면 0.
- magic = [(마법의 방향 di, 거리 si)]
- direction_cnt = [i//2 for i in range(2, N*2)] + [N-1] # 마지막에 '서'로 끝나기 때문에 하나 추가
- dxy = shell용 반시계 회오리 방향

# 구슬 배열 1D 변환
- cur_list = [0] * (N*N) 
- x, y = N//2, N//2 # 마법사 상어 위치
- d = 0 # 좌측 시작
- for direction_cnt:
    - for range(dc):
        - cur_list[cnt] = arr[y][x] 
        - cur_idx ++
    - d = (d+1)%4 # 방향 전환

# 1D(cur_list) 기준 파괴될 대상의 idx 구성
- plus = 2
- icebreak_idx_in_cur = [0] * (N//2)*4
- icebreak_idx_in_cur[0] = 1
- for i in range(1, (N//2)*4): # shell개수 = N//2. 4방 번걸아가며 계산
    - icebreak_idx_in_cur[i] = icebreak_idx_in_cur[i-1] + plus
    - if i%4 in (0, 3): # (북 -> 서), (서 -> 남) 전환시 +1씩 증 
        - plus ++

# dxy[d_map[idx]] _, ↑, ↓, ←, →. 문제용 -> shell용 ←, ↓, →, ↑. 매핑.
- d_map = [0, 3, 1, 0, 2 ] dxy 매핑 테이블
- marvel_cnt = [0] * 4 폭발한 idx 구슬의 개수 리스트  
- for d, s in magic: # 방향, 거리
    - d = d_map[d]
    - cnt = 0
    # icebreak_idx_in_cur(1D)에서 방향d에 따라 구슬 삭제
    - for idx in range(0, len(icebreak_idx_in_cur)):  
        - if cnt >= s: 구슬 삭제 cnt = shell level = s
            - break
        - if (idx%4) == d: idx는 4번에 한번 마법방향 d와 일치 
            - cur_list에서 구슬 삭제(0)
            - cnt ++
    # 구슬 이동
    - cur_list = move_marvel(cur_list)
    # 동일 숫자 구슬 파괴
    - while (explosion()):
        # 구슬 이동
        - cur_list = move_marvel()
    # cur_list update
    - cur_list = change_list()

# 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)
- print(marvel_cnt[1]+2*marvel_cnt[2]+3*marvel_cnt[3])

- move_marvel(cur_list):
    - while 0 in cur_list:
        - cur_list.remove(0) 파괴된 구슬(0) 제거
    - cur_list = [0] + cur_list + [0] * (N*N - len(cur_list) - 1) 맨앞은 0, 나머지 뒷부분 0 채우기
    - return cur_list

- explosion():
    - flag = 0
    - start = 1
    - end = 2
    - while (start <= end < N*N):
        - if cur_list[start] != cur_list[end]: 다르면 폭발 여부 확인 
            - if (end - start) > 3: # 4개 이상 연속
                - for idx in range(start, end):
                    - flag = 1 폭팔 
                    # 폭발 개수를 구슬 idx에 따라 구분하여 marvel_cnt 리스트에 기록
                    - marvel_cnt[cur_list[start]] += end - start 
                    - cur_list[idx] = 0 구슬 제거
            - start = end 재설정
            - end = start + 1 재설정
        - else: 같으면 end 지점 확장 
            end += 1
    return flag

- change_list():
    - new_cur_list = [0] * (N*N)
    - idx = 1
    - start = 1
    - end = 2
    - while (start <= end < N*N and idx < N*N):
        if cur_list[start] != cur_list[end]: 다르면 계산
            - new_cur_list[idx] = end-start 개수 기록
            - new_cur_list[idx + 1] = cur_list[start] 구슬 번호 기록
            - idx += 2
            - start = end
            - end = start + 1
        - else: 같으면 end 지점 확장 
            - end += 1
    - return new_cur_list 


'''

def move_marvel(cur_list):
    while 0 in cur_list:
        cur_list.remove(0)
    cur_list = [0] + cur_list + [0] * (N*N - len(cur_list) - 1)
    return cur_list

def explosion():
    flag = 0
    start = 1
    end = 2
    while (start <= end < N*N):
        if cur_list[start] != cur_list[end]:
            if (end - start) > 3:
                for idx in range(start, end):
                    flag = 1
                    marvel_cnt[cur_list[start]] += end - start
                    cur_list[idx] = 0
            start = end
            end = start + 1
        else:
            end += 1
    return flag

def change_list():
    new_cur_list = [0] * (N*N)
    idx = 1
    start = 1
    end = 2
    while (start <= end < N*N and idx < N*N):
        if cur_list[start] != cur_list[end]:
            new_cur_list[idx] = end-start
            new_cur_list[idx + 1] = cur_list[start]
            idx += 2
            start = end
            end = start + 1
        else:
            end += 1
    return new_cur_list

N, M = map(int, input().split()) # 격자크기 N(idx 1부터 시작), 블리자드 M번.
arr = [list(map(int, input().split())) for _ in range(N)] # 격자에 들어 있는 구슬 정보. 없으면 0. 상어 있으면 0.
magic = [list(map(int, input().split())) for _ in range(M)] # 블리자드 마법의 방향 di, 거리 si.

direction_cnt = [i//2 for i in range(2, N*2)]
direction_cnt.append(N-1)
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6]
dx = [-1, 0, 1, 0] # shell용 반시계 방향 ←, ↓, →, ↑
dy = [0, 1, 0, -1]
cur_list = [0] * (N*N) # 구슬 배열 1D 변환용
cur_idx = 1
x, y = N//2, N//2 # 마법사 상어 위치
d = 0
for dc in direction_cnt:
    for _ in range(dc):
        x, y = x+dx[d], y+dy[d]
        cur_list[cur_idx] = arr[y][x] # 상어에서 시작, 구슬 배열 1D로 재구성.
        cur_idx += 1
    d = (d+1)%4

# 1D(cur_list) 기준 파괴될 대상의 idx 구성
plus = 2
icebreak_idx_in_cur = [0] * (N//2)*4
icebreak_idx_in_cur[0] = 1
for i in range(1, (N//2)*4): # shell개수 = N//2. 4방 번걸아가며 계산
    icebreak_idx_in_cur[i] = icebreak_idx_in_cur[i-1] + plus
    if i%4 in (0, 3):
        plus += 1

d_map = [0, 3, 1, 0, 2] # dxy 매핑 테이블
marvel_cnt = [0] * 4 # 폭발한 idx 구슬의 개수 리스트
for d, s in magic:
    d = d_map[d]
    cnt = 0
    for idx in range(0, len(icebreak_idx_in_cur)):
        if cnt >= s:
            break
        if (idx%4) == d:
            cur_list[icebreak_idx_in_cur[idx]] = 0
            cnt += 1

    cur_list = move_marvel(cur_list)
    while explosion():
        cur_list = move_marvel(cur_list)
    cur_list = change_list()

# 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)
print(marvel_cnt[1]+2*marvel_cnt[2]+3*marvel_cnt[3])