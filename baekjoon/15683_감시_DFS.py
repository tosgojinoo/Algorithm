def watch_case(x, y, case):
    watch_area = set() # 중복 제거
    for d in case:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if not 0<=nx<N or not 0<=ny<M or arr[nx][ny] == 6: # 범위 밖 or 벽
                break
            elif arr[nx][ny] == 0:
                watch_area.add((nx, ny))
    return watch_area

def DFS(depth, prev_set):
    global watched_set
    if depth == len(cctv):
        if len(prev_set) > len(watched_set): # 더 많이 비추면 갱신
            watched_set = prev_set
        return
    for cur_set in cctv[depth]: # 조합1, 조합2..
        DFS(depth+1, prev_set|cur_set) # prev_set | 조합1


cam_type = {
    1:[[0], [1], [2], [3]],
    2:[[0, 1], [2, 3]],
    3:[[0, 2], [0, 3], [1, 2], [1, 3]],
    4:[[0, 1, 2], [0, 1, 3], [2, 3, 0], [2, 3, 1]],
    5:[[0, 1, 2, 3]]
}
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

blind = 0
cctv = []
cctv_idx = 0
dx = [0, 0, -1, 1] # 오, 왼, 상, 하
dy = [1, -1, 0, 0] 

# cctv별로 비출 수 있는 경우의 수 set 조합들 만들어 cctv에 저장.
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            blind += 1 # 안보이는 지역 수
        elif arr[i][j] != 0 and arr[i][j] != 6: # 캠 있는 지역
            cctv.append([])
            for case in cam_type[arr[i][j]]:
                cctv[cctv_idx].append(watch_case(i, j, case)) # 경우마다 비춰지는 좌표들 set

            cctv_idx += 1

# 가장 넓은 범위로 비추는 watched_set 만들기
watched_set = set()
DFS(0, set())
print(blind - len(watched_set))