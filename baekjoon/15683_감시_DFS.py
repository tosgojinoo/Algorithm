'''
[설명]
N×M
K개의 CCTV
- CCTV는 5가지 종류
    - 1번 CCTV는 한 쪽 방향
    - 2번과 3번은 두 방향
        - 2번은 감시하는 방향이 서로 반대방향
        - 3번은 직각 방향
    - 4번은 세 방향
    - 5번은 네 방향

CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시
사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없음
CCTV가 감시할 수 없는 영역은 사각지대

- CCTV는 회전
    - 회전은 항상 90도
    - 감시하려고 하는 방향이 가로 또는 세로 방향

0은 빈 칸, 6은 벽, 1~5는 CCTV 종류
CCTV의 최대 개수는 8개를 넘지 않음

[문제]
사각 지대의 최소 크기 -> 감시 최대 범위, 경우의 수 DFS
'''
'''
[알고리즘]
- ccvt 볼 수 있는 영역의 경우의 수 구성 > cctv별 조합 > 가장 넓은 범위로 비추는 조합 선벼 
- dxy: 오, 왼, 상, 하
- cam_type
    - 캠별 방향 경우의 수 계산
    - 단일 설정에서 가능한 방향 & 90도씩 회전시 가능한 방향
- cctv 
    - idx = cctv_idx
    - value = 비출 수 있는 구역의 경우의 수

- watch_case(i, j, case) 
    - watch_area
        - set()
        - cctv 방향 경우의 수 > while True > 빈공간 > watch_area 추가  

- DFS(cctv_idx, watched_set)
    - cctv_idx 별 감시 영역 조합 선택 > DFS(cctv_idx+1, watched_set|case) > 모든 cctv 확인 후 결과 저장
    - watched_set|case == 감시 영역 합계

- 결과: blind - watched_set
'''
'''
[구조]
- cam_type = {
    1:[[0], [1], [2], [3]],
    2:[[0, 1], [2, 3]],
    3:[[0, 2], [0, 3], [1, 2], [1, 3]],
    4:[[0, 1, 2], [0, 1, 3], [2, 3, 0], [2, 3, 1]],
    5:[[0, 1, 2, 3]]
}

- arr 저장
- blind = 안보이는 지역의 수
- cctv = cctv별 비출 수 있는 구역의 경우의 수 set 조합 저장
- cctv_idx = 0
- dxy = 오, 왼, 상, 하

# cctv 경우의 수 구성
- for 전체 탐색
    - if 빈칸:
        - blind ++
    - elif 캠: 
        - for cam_type[arr[i][j]]:
            # 경우마다 비춰지는 좌표들 set
            - cctv[cctv_idx] 추가 watch_case(i, j, case) 

        - cctv_idx ++

# 가장 넓은 범위로 비추는 케이스 만들기
- result = set()
- DFS(0, set())
- print(blind - len(result))


- watch_case(x, y, case):
    - watch_area = set()
    - for case:
        - while True:
            - nxy 업데이트
            - if 범위 밖 or 벽: break
            - elif 빈공간:
                - watch_area 추가 (nx, ny)
    - return watch_area

- DFS(cctv_idx, watched_set):
    - if cctv_idx == len(cctv):
        - if len(watched_set) > len(result):
            - result = watched_set
        - return
    - for cctv[cctv_idx]: cctv별 감시 영역 조합
        - DFS(cctv_idx+1, watched_set|case)
'''


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
            elif not arr[nx][ny]:
                watch_area.add((nx, ny))
    return watch_area

def DFS(cctv_idx, watched_set):
    global result
    if cctv_idx == len(cctv):
        if len(watched_set) > len(result): # 더 많이 비추면 갱신
            result = watched_set
        return
    for case in cctv[cctv_idx]: # 조합1, 조합2..
        DFS(cctv_idx+1, watched_set|case) # watched_set | 조합1


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
        if not arr[i][j]: # 빈칸
            blind += 1
        elif arr[i][j] not in (0, 6): # 캠
            cctv.append([])
            for case in cam_type[arr[i][j]]:
                cctv[cctv_idx].append(watch_case(i, j, case)) # 경우마다 비춰지는 좌표들 set

            cctv_idx += 1

# 가장 넓은 범위로 비추는 result 만들기
result = set()
DFS(0, set())
print(blind - len(result))