def move_marvel():
    new_list = [0] * (N*N)
    cnt = 1
    for i in range(1, N*N):
        if cur_list[i]:
            new_list[cnt] = cur_list[i]
            cnt += 1
    return new_list

def explosion():
    flag = 0
    start = 1
    end = 2
    while(start < N*N and end < N*N):
        if cur_list[start] != cur_list[end]:
            if (end - start) > 3:
                for i in range(start, end):
                    flag = 1
                    marvel_cnt[cur_list[start]] += end - start
                    cur_list[i] = 0
            start = end
            end = start + 1
        else:
            end += 1
    return flag

def change_list():
    new_list = [0] * (N*N)
    start = 1
    end = 2
    cnt = 1
    while (start < N*N  and end < N*N and cnt < N*N):
        if cur_list[start] != cur_list[end]:
            new_list[cnt] = end-start
            new_list[cnt + 1] = cur_list[start]
            cnt += 2
            start = end
            end = start + 1
        else:
            end += 1
    return new_list

N, M = map(int, input().split()) # 격자크기 N(idx 1부터 시작), 블리자드 M번.
arr = [list(map(int, input().split())) for _ in range(N)] # 격자에 들어 있는 구슬 정보. 없으면 0. 상어 있으면 0.
magic = [list(map(int, input().split())) for _ in range(M)] # 블리자드 마법의 방향 di, 거리 si.

direct_cnt = [i//2 for i in range(2, N*2)]
direct_cnt.append(N-1)
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6]
dx = [-1, 0, 1, 0] # 반시계 회오리 방향 ←, ↓, →, ↑    # 문제는 ↑, ↓, ←, →. 입력 idx는 1부터 시작.
dy = [0, 1, 0, -1]
cur_list = [0] * (N*N) # 구슬 배열 1D 변환용
cnt = 1
x, y = N//2, N//2 # 마법사 상어 위치
d = 0
for dc in direct_cnt:
    for i in range(dc):
        x, y = x+dx[d], y+dy[d]
        cur_list[cnt] = arr[y][x] # 상어에서 시작, 구슬 배열 1D로 재구성.
        cnt += 1
    d = (d+1)%4


marvel_cnt = [0] * 4 # 폭발한 idx 구슬의 개수 리스트
plus = 2
ice_break_idx = [0] * (N//2)*4
ice_break_idx[0] = 1
for i in range(1, (N//2)*4):
    ice_break_idx[i] = ice_break_idx[i-1] + plus
    if i%4 == 0 or i%4 == 3:
        plus += 1

d_map = [0, 3, 1, 0, 2 ]
for d, s in magic:
    d = d_map[d]
    cnt = 0
    for i in range(0, (N//2)*4):
        if cnt >= s:
            break
        if (i%4) == d:
            cur_list[ice_break_idx[i]] = 0
            cnt += 1
    cur_list = move_marvel()
    while (explosion()):
        cur_list = move_marvel()
    cur_list = change_list()

print(marvel_cnt[1]+2*marvel_cnt[2]+3*marvel_cnt[3]) # 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)