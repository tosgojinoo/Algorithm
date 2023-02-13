'''
dir = [(x-1)/y, x-1/y-1, x/y-1, ...,x+1/y-1]

move_fish(x, y, dir):
- nx, ny = x, y + dxy
- arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]

change_fish():
- for fish_idx in len(fish_list):
    if fish_list[fish_idx]:
    - dir = fish_list[fish_idx]
    - move_fish(i, j, dir)

main
- arr = [[False]*N for _ in range(N)]
- fish_list = [1~N**2]
- for i in range(4):
    - input_seq = map(int, input().split())
    for j in range(1,5):
        - idx, dir = input_seq[(j-1)*2:j*2]
        - arr[i][j-1] = (idx, dir)
        - fish_list[idx] = i, j, dir

dir_init = arr[0][0][1]
shark = (0, 0, dir_init)
arr[0][0] = (0,0)

while 상어 이동 가능: -> X => DFS 로 풀어야함
    change_fish()
'''

def find_fish(fish_idx, arr):
    for i in range(SIZE):
        for j in range(SIZE):
            if arr[i][j][0] == fish_idx:
                return i, j
    return -1, -1


def swap_all_fish(r, c, arr):
    for fish_idx in range(1, SIZE * SIZE + 1): #
        fish_r, fish_c = find_fish(fish_idx, arr) # idx에 맞는 fish 좌표 확인
        if fish_r == fish_c == -1: # fish_idx 없으면 return -1,-1. 무시
            continue
        d = arr[fish_r][fish_c][1] # 찾은 fish의 방향
        for add_d in range(DSIZE): # fish 갈자리 보기
            nd = (d + add_d) % DSIZE
            fish_nr = fish_r + dr[nd]
            fish_nc = fish_c + dc[nd]
            if not (0<=fish_nr<SIZE) or not (0<=fish_nc<SIZE): # 범위 밖 무시
                continue
            if fish_nr == r and fish_nc == c: # 상어자리 무시
                continue
            arr[fish_r][fish_c][1] = nd # ***** 새롭게 얻은 방향 적용
            arr[fish_r][fish_c], arr[fish_nr][fish_nc] = arr[fish_nr][fish_nc], arr[fish_r][fish_c] # 자리 스위칭
            break


def DFS(r, c, sum_values, arr):
    global ans
    sum_values += arr[r][c][0] # fish_idx 저장
    ans = max(ans, sum_values)
    arr[r][c][0] = 0 # fish 삭제

    swap_all_fish(r, c, arr) # fish 위치 변경

    d = arr[r][c][1] # fish 방향 -> 상어 방향 전이
    while True: # 동일 방향 내 갈수 있는 모든 위치로 이동 후 DFS
        r += dr[d] # 1배씩 증가
        c += dc[d]
        if not (0<=r<SIZE) or not (0<=c<SIZE): # 범위 밖 종료. 집으로.
            break
        if arr[r][c][0] == 0: # fish_idx 가 비어있을 경우 무시
            continue

        # tmp = []
        # for i in range(SIZE):
        #     tmp.append([])
        #     for j in range(SIZE):
        #         tmp[i].append(arr[i][j].copy())
        DFS(r, c, sum_values, [[c[:] for c in l] for l in arr]) # 3차원 복사 방법 주의


SIZE = 4
DSIZE = 8
dr = (-1, -1, 0, 1, 1, 1, 0, -1) # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dc = (0, -1, -1, -1, 0, 1, 1, 1)


arr = [[] for _ in range(SIZE)]
for i in range(SIZE):
    info = list(map(int, input().split()))
    for j in range(SIZE):
        arr[i].append([info[j * 2], info[j * 2 + 1] - 1]) # dir을 0 기준으로 바꾸기 위해 -1

ans = 0
DFS(0, 0, 0, arr) # r, c, sum_values, arr

print(ans)