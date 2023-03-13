'''
[설명]
N×N
격자의 각 칸에는 바구니가 하나
바구니에 저장할 수 있는 물의 양에는 무제한
(r, c)는 격자의 r행 c열에 있는 바구니
A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양
가장 왼쪽 윗 칸은 (1, 1)
가장 오른쪽 아랫 칸은 (N, N)
마법사 상어는 연습을 위해 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다.
N번 행의 아래에는 1번 행
1번 행의 위에는 N번 행
1번 열의 왼쪽에는 N번 열
N번 열의 오른쪽에는 1번 열

비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생성
이제 구름에 이동을 M번 명령하려고 한다.
i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다.
방향은 총 8개의 방향. 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. -> dxy 제한

- 이동 명령
    - 모든 구름이 di 방향으로 si칸 이동
    - 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가
    - 구름이 모두 사라짐
    - 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전
        - 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가
        - 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
        - 예) (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)
             (N, N)에서 인접한 대각선 칸은 (N-1, N-1)
    - 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 감소
    - 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 함

[문제]
M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합
'''
'''
[알고리즘]
- dxy: 8방향. 문제 조건.
- arr
    - 4방 끝단이 반대편과 이어지는 주기 회전 방식 -> (x % 총길이) 수식 적용
    - 행 
        - (r + dis*dx[dir]) % n 
    - 열
        - (c + dis*dy[dir]) % n
- 대각선만 확인
    - for i in range(1, 8, 2): # 2칸씩 이격
'''
'''
[구조]
- arr = 물의 양 저장
- move_cloud = 이동 M commands 저장용 (idx -1 적용)

- for M번 이동:
    - d, s = (구름이 di 방향으로, si칸 이동)
    - move_cloud에 (d-1, s) 저장. d는 idx -1 shift.
    
- dxy = 9시 부터 시계방향
- cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)] # 구름 생성 위치(문제 제시). 입력 idx는 1부터, shift -1 하여 계산은 0부터.

- for 구름 이동 횟수:
    - visited 초기화
    - rain(move_cloud(방향), move_cloud(이동칸수))
    - cloud = 구름 초기화
    - for 전체 탐색:
        - if 미방문, 물이 2이상:
            - cloud.append((i, j)) 구름 추가 
            - arr[i][j] -= 2 # 물 양 감소

- print(sum(map(sum, arr)))

- rain(dir, dis):
    - moved_cloud = 이동 완료된 구름들 저장용
    - for 구름 있는 위치들:
        - nr = (r + dis*dx[dir]) % n
        - nc = (c + dis*dy[dir]) % n
        - arr[nr][nc] ++= 이동 완료 구름 위치에 물 추가
        - visited[nr][nc] = 방문 처리
        - moved_cloud.append((nr, nc)) 이동 완료 구름 저장
    - for 이동 완료 구름 위치들:
        - for 대각선만 확인:
            - if 범위내, 물 있을 경우:
                - arr[r][c] += 1 # 물 추가

'''


def rain(dir, dis):
    moved_cloud = []
    for r, c in cloud: # 구름 있는 위치들
        nr = (r + dis*dx[dir]) % n # 격자의 양 끝단이 이어져 있는 형태
        nc = (c + dis*dy[dir]) % n
        arr[nr][nc] += 1 # 이동한 구름 위치에 물 추가
        visited[nr][nc] = 1 # 방문 처리
        moved_cloud.append((nr, nc))
    for r, c in moved_cloud:
        for i in range(1, 8, 2): # 대각선만 확인
            nr = r + dx[i]
            nc = c + dy[i]
            if 0<=nr<n and 0<=nc<n and arr[nr][nc]: # 범위내, 물 있을 경우
                arr[r][c] += 1 # 물 추가


n, m = map(int,input().split()) # 격자 N, 구름이동 M
arr = [list(map(int,input().split())) for _ in range(n)] # 물의 양
move_cloud = []

for i in range(m):
    d, s = map(int,input().split()) # 구름이 di 방향으로, si칸 이동
    move_cloud.append([d-1, s]) # d의 입력 idx는 1부터, shift -1 하여 계산은 0부터.
dx = [0, -1, -1, -1, 0, 1, 1, 1] # 9시 부터 시계방향
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)] # 구름 생성 위치. 입력 idx는 1부터, shift -1 하여 계산은 0부터.

for d in range(m):
    visited = [[0] * n for _ in range(n)]
    rain(move_cloud[d][0], move_cloud[d][1])
    cloud = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > 1: # 미방문, 2이상 칸에 구름 생성
                cloud.append((i, j)) # 구름 추가
                arr[i][j] -= 2 # 물 양 감소

print(sum(map(sum, arr)))