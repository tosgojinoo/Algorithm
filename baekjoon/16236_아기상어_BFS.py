'''
[설명]
N×N 크기
물고기 M마리와 아기 상어 1마리

가장 처음에 아기 상어의 크기는 2
아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고,
나머지 칸은 모두 지나갈 수 있다.
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

- 아기 상어가 어디로 이동할지 결정하는 방법
    - if 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청
    - if 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 감
    - else 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 감 -> 가장 가까운 거리 BFS
        - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값
            - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹음

아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정
아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다.
물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가

- 공간의 상태
    - 0: 빈 칸
    - 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
    - 9: 아기 상어의 위치
    - 아기 상어는 공간에 한 마리

[문제]
아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간 -> while 대상 발견:
'''
'''
[알고리즘]
- baby_shark
    - 상어 정보 저장
    - (shark_size, exp, i, j)

- while True:
    - 거리, 좌표 = BFS(상어 정보)
    - 거리 추가 
    - 잡은 물고기수와 shark_size 비교
    - 물고기 제거, shark 정보 갱신

- BFS
    - 현 지점 기준 최근거리 물고기 찾기
    - queue = [(dist, i, j)]
    - deque 미사용 
    - min(queue)로 최소 가중치(거리) 순으로 호출
        - 호출 후 queue.remove(min(queue)) 필수
    - 이동
        - 우선순위
            - 위 > 좌
            - if 조건을 먼저 작성
            - or, dxy에 (위, 좌, 우, 하) 순서 적용
    - 미 발견시, -1 flag 처리

'''
'''
[구조]
- arr = 저장
- for 전체 탐색
    - baby_shark = (2, 0, i, j) # (shark_size, exp, i, j)

- while True:
    - 상어 정보 불러오기
    - dist, i, j = BFS(i, j)

    - if 미 발견시 i == -1: break

    - time += dist
    - exp ++ 잡은 물고기 개수
    - if exp >= shark_size:
        - shark_size += 1
        - exp = 초기화
    - arr[i][j] = 물고기 제거
    - baby_shark = (shark_size, exp, i, j)
- print(time)


- BFS(i, j):
    - queue = [(0, i, j)] # dist, i, j

    - while queue:
        - dist, i, j = min(queue) # 거리 가장 가까운 순서
        - queue.remove((dist, i, j))
        
        # 지나갈 수 있는 범위 인지. (크기 동일, 빈칸, 본인)        
        - if arr[i][j] in (0, shark_size, 9):  
            # 우선순위(위 -> 왼) 적용
            - for ni, nj in [((i - 1), j), (i, (j - 1)), (i, (j + 1)), ((i + 1), j)]:
                - if 범위내 and 미방문:
                    - queue 추가 (dist + 1, ni, nj)
                    - visited[ni][nj] = 방문처리
        - elif 본 크기보다 작은 물고기 발견:
            - return dist, i, j

    - return (0, -1, -1) # 미발견시
'''



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
    queue = [(0, i, j)]  # dist, i, j
    visited = [[False] * N for _ in range(N)]
    visited[i][j] = True

    while queue:
        dist, i, j = min(queue)
        queue.remove((dist, i, j))

        if arr[i][j] in (0, shark_size, 9):  # 현 위치가 지나갈 수 있는 범위. 크기 동일, 빈칸, 본인.
            # 우선순위(위 -> 왼) 적용
            for ni, nj in [((i - 1), j), (i, (j - 1)), (i, (j + 1)), ((i + 1), j)]:
                if 0<=ni<=N-1 and 0<=nj<=N-1 and not visited[ni][nj]:
                    queue.append((dist + 1, ni, nj))
                    visited[ni][nj] = True
        elif arr[i][j] < shark_size:  # 본 크기보다 작은 물고기 발견시 리턴
            return dist, i, j

    return (0, -1, -1)  # 미발견시



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