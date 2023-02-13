''' my idea
상어 크기 2, 자신의 크기와 같은 수를 먹을 때마다 1 증가
이동 방법
- 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청 => 종료 조건
- 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
- 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다. => 우선 순위
    - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
    - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다. => 우선 순위
우선 순위
- 근 거리(칸 개수) -> 위 -> 왼쪽 순서

변수
- 상어 크기 shark_size
- 물고기 크기 우선순위 queue(크기, y, x) -> x => BFS 에서 바로 적용
- arr
- 이동 cnt -> dist
- 잡은 물고기 exp
- visited
- 미발견시 flag or -1


BFS()
- if size > size_limit:
    return
- for d in range(4):
    - nx,ny = x,y + dxy

main
- target_list = []
- arr 저장
    - start: 9 위치
    - target_list[size].append(1~6 숫자 위치(y, x))
    -

size_limit = 1
Dijkstra() -> x => BFS()로 충분. 최근거리 계산 효과 있기 때문.

'''
def BFS(i, j):
    queue = [(0, i, j)] # dist, i, j
    visited = [[False] * N for _ in range(N)]
    visited[i][j] = True

    while len(queue) > 0:
        dist, ni, nj = min(queue)
        queue.remove((dist, ni, nj))

        if arr[ni][nj] == shark_size or arr[ni][nj] == 0 or arr[ni][nj] == 9: # 현 위치가 지나갈 수 있는 범위. 크기 동일, 빈칸, 본인.
            # 우선순위(위 -> 왼) 적용. 4방향 루프 미사용. 방향별 범위 제한 다름.
            if ni > 0 and not visited[ni - 1][nj]: # 위
                queue.append((dist + 1, ni - 1, nj))
                visited[ni - 1][nj] = True
            if nj > 0 and not visited[ni][nj - 1]: # 좌
                queue.append((dist + 1, ni, nj - 1))
                visited[ni][nj - 1] = True
            if nj < N - 1 and not visited[ni][nj + 1]: # 우
                queue.append((dist + 1, ni, nj + 1))
                visited[ni][nj + 1] = True
            if ni < N - 1 and not visited[ni + 1][nj]: # 아래
                queue.append((dist + 1, ni + 1, nj))
                visited[ni + 1][nj] = True
        elif arr[ni][nj] < shark_size: # 본 크기보다 작은 물고기 발견시 리턴
            return dist, ni, nj

    return (0, -1, -1) # 미발견시



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            baby_shark = (2, 0, i, j) # shark_size, exp, i, j
            break

time = 0
while True:
    shark_size, exp, i, j = baby_shark
    dist, i, j = BFS(i, j)

    if i < 0: # 미발견시 return -1에 대한 것
        break

    time += dist
    exp += 1 # 단순히 잡은 물고기 개수
    if exp >= shark_size:
        shark_size += 1
        exp = 0
    arr[i][j] = 0 # 물고기 제거
    baby_shark = (shark_size, exp, i, j)

print(time)