# 높이 정보 저장
# 1스텝마다, 높이 - (동서남북 네방향에 붙어있는 0의 칸 개수)
# 0이 최저
# 두 덩어리 이상으로 분리되는 최소의 시간

# [순서]
# 0) step 반복
# 1) i, j 순회
# 2) arr[i][j]>0 일 때 처리1
# 3) 처리1> 4방을 확인하고, 0이 있는 맞큼 높이 차감 (visited 필요)
# 4) 처리2> 처리1 모두 종료 후 4방향 확인,
#   a) 방법1> 4방향 모두 0일 경우 cnt +=1
#   b) 방법2> bfs로 다 돌았는데, 전부 돈 것이 아닐 경우 (visited2 필요)

# [종료]
# 1) result >=2 이면, return step
# => (변경) BFS 카운팅용 len(result) >=2 면 year 출력, 아니면, 0 출력(전부 다 녹을때까지 BFS가 1회만 돌았을 경우(한덩어리, 다음 year에 len(result)==0)

# [제한]
# 처리1 이 끝난 후에야 덩어리 확인 가능
# 동일 step 내에서, 이전 melted에서 0이 되버리면 다음 노드에 영향을 줌(영향 주면 안됨) => melted 함수 미사용, visited로 구분 가능

# [체크]
# bfs가 dfs 대비 빠를 것 같음
# (추가) dfs의 경우 recursionlimit(10**5)로 줄여서 적용해야함, 그래도 메모리 에러 발생, pypy3는 recursion에 메모리 사용량 큼
# 우선순위q x, 가중치q(appendleft) x

# [주의사항]
# bfs > while q > if visited 빼먹지 말기
# "melted" 함수를 따로 구성할 경우, 4방향 확인 반복으로 시간 초과 발생
# 다 녹을때까지 빙산이 한덩어리 일 수도 있음, 출력에 반드시 반영해야함
# *** BFS 횟수만 저장하는 result 필요
# *** visited 위치 중요
# ***** [가장 중요!] BFS가 1회 초과할 경우 바로 중지해야 함


import sys
from collections import deque
input = sys.stdin.readline

def BFS(y, x):
    global arr, visited
    q = deque([(y, x)])
    visited[y][x] = 1

    while q:
        y, x = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<M and visited[ny][nx] == 0: # 범위 내, 방문 여부 확인 후, *** visited 위치 중요
                if arr[ny][nx] == 0: # 0이면 얼음 녹이기
                    if arr[y][x] >0:
                        arr[y][x] -= 1
                elif arr[ny][nx] != 0: # 숫자면 q 추가
                    q.append((ny, nx))
                    visited[ny][nx] = 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
year = 0
while True:
    year += 1
    result = []
    visited = [[0] * M for _ in range(N)] # *** visited 위치 중요

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visited[i][j] == 0: # *** visited 위치 중요
                result.append([BFS(i, j)])

    if len(result) >1 or len(result)==0: # ***** [가장 중요!] BFS가 1회 초과 or 0회(이전까지 BFS 1회고, 전부다 녹음)할 경우 바로 중지해야 함
        break

print(year-1 if len(result)>=2 else 0)