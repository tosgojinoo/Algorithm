'''
[설명]
2^N × 2^N
(r, c)
A[r][c]는 (r, c)에 있는 얼음의 양
A[r][c]가 0인 경우 얼음 없음

- 단계 L
    - 2^L × 2^L 크기의 부분 격자로 분할 -> rotate()
    - 모든 부분 격자를 시계 방향으로 90도 회전 -> rotate()
    - 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 감소 -> melt()
        - (r, c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)

- Q번 시전
    - 남아있는 얼음 A[r][c]의 합
    - 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
    - 얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면, 두 칸을 연결되어 있다고 한다. 덩어리는 연결된 칸의 집합 -> BFS

[문제]
남아있는 얼음 A[r][c]의 합
가장 큰 덩어리가 차지하는 칸의 개수
    단, 덩어리가 없으면 0
'''
'''
[알고리즘]
- rotate()
    - 90도 회전 결과 저장용 arr_new 준비
    - 90도 행렬 회전
        - N - 1 - 회전 전의 행 번호 (r 역순) -> dr = 회전 후의 열 번호
        - 회전 전의 열 번호 (c 정순) -> dc = 회전 후의 행 번호
        - arr[i + (s -1 -x)][j + y] -> arr_new[i + y][j + x]
'''
'''
[구조]
- arr = 칸 별 얼음양 저장
- order = 시전한 단계 L1, L2, ..., LQ 저장
- for order:
    - rotate(order[i])
    - melt()

- print(sum(map(sum, zip(*arr))))
- print(BFS())

- rotate(order):
    - if not order: 중지

    - s = 2 ** order # 단위 크기
    - arr_new = arr 크기 동일한 빈 array. 90도 회전 저장용.
    - for 전체 탐색, 단위 크기만큼씩:
        - for 단위크기 내에서 (x, y) 탐색:
            - arr_new[i + y][j + x] = arr[i + (s -1 -x)][j + y] # 90도 회전
    - arr = arr_new

- melt():
    - arr_copy
    - for 전체 탐색:
        - cnt = 주위 얼음수 계산용
        - if 얼음 있으면:
            - for 4방:
                - if 범위 내:
                    - if 얼음 있으면:
                        - cnt ++
            - if cnt 주위 얼음수 3 미만:
                - arr_copy[x][y] -= 1 # 차감
    - arr = arr_copy

# 가장 큰 덩어리 칸의 개수 구하기
- BFS(): 
    - MAX = 최대 개수 저장용
    - visited 초기화
    - for 전체 탐색:
        - if 미방문 and 얼음 있음:
            - 방문 처리
            - queue = deque([(x, y)])
            - cnt = 한 덩어리 내 얼음칸 cnt 용
            - while queue:
                - for 4방:
                    - if 범위 내:
                        - if 미방문 and 얼음 있음:
                            - 방문 처리
                            - queue 추가
                            - cnt += 1

            - MAX = 최대 cnt 저장
    - return MAX
'''


from collections import deque

def rotate(order):
    global arr
    if not order: # order == 0
        return
    s = 2 ** order
    arr_new = [[0] * N for _ in range(N)] 
    for i in range(0, N, s):
        for j in range(0, N, s):
            for x in range(s):
                for y in range(s):
                    arr_new[i + y][j + x] = arr[i + (s - 1 - x)][j + y] # 수식 중요.
    arr = arr_new
    return

def melt():
    global arr
    arr_copy = [i[:] for i in arr]
    for x in range(N):
        for y in range(N):
            cnt = 0 # 주위 얼음수
            if arr[x][y]: # 얼음 있으면.
                for d in range(4): # 4방 확인
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N: # 범주 내면
                        if arr[nx][ny]: # 얼음 있으면
                            cnt += 1
                if cnt < 3: # 주위 얼음수 3 미만이면.
                    arr_copy[x][y] -= 1 # 차감
    arr = arr_copy
    return


def BFS(): # 가장 큰 덩어리 칸의 개수 구하기
    MAX = 0
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and arr[x][y]:
                visited[x][y] = True
                queue = deque([(x, y)])
                cnt = 1
                while queue: # 한 덩어리 내 얼음칸 cnt
                    x, y = queue.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and arr[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                cnt += 1

                MAX = max(MAX, cnt)
    return MAX

n, m = map(int, input().split()) # 사이즈 N. Q번 시전.
N = 2 ** n
arr = [list(map(int, input().split())) for _ in range(N)] # 얼음양
order = list(map(int, input().split())) # 시전한 단계 L1, L2, ..., LQ

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(m):
    rotate(order[i])
    melt()

print(sum(map(sum, zip(*arr))))
print(BFS())