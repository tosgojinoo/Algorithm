def Find_block():
    visited = [[arr[i][j] < 0 for j in range(N + 2)] for i in range(N + 2)] # -1 벽은 True 방문 처리
    max_block = (0, 0, 0, 0, []) # max 우선순위: 가장 큰 블록(len(queue) > 가장 많은 무지개(len(rainbow)) > 기준 행값 > 기준 열값. 마지막에 queue를 함께 저장해 전달.

    for i in range(1, N + 1):
        for j in range(1, N + 1): # 전체 탐색하며, 계산 대상 선정
            if visited[i][j] or not arr[i][j]: # 방문 했거나, arr == 0(무지개 블록) 이면 무시.
                continue

            block_num = arr[i][j]
            visited[i][j] = True
            queue = [(i, j)] # 거쳐간 데이터들 재사용 할 것이기 때문에, not deque.
            rainbow = []
            idx = 0
            while idx < len(queue):
                i, j = queue[idx]
                idx += 1
                for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if not visited[ni][nj]: # 미방문
                        if not arr[ni][nj]: # 무지개 블록
                            visited[ni][nj] = True # 방문처리
                            rainbow.append((ni, nj))
                            queue.append((ni, nj))
                        elif arr[ni][nj] == block_num: # 동일 블록 숫자
                            visited[ni][nj] = True
                            queue.append((ni, nj))

            max_block = max(max_block, (len(queue), len(rainbow), i, j, queue)) # max 우선순위: 가장 큰 블록(len(queue) > 가장 많은 무지개(len(rainbow)) > 기준 행값 > 기준 열값. 마지막에 queue를 함께 저장해 전달.

            for i, j in rainbow: # 계산에 포함된 무지개 블록은, visited 초기화
                visited[i][j] = False

    return max_block[-1]


def Gravity():
    for j in range(1, N + 1): # 열 순서대로 정렬.
        floor = N + 1 # 정렬 기준 바닥
        for i in range(N, 0, -1): # 행. 밑에서부터 역순. 맨 아래줄(N+1)은 제외.
            if arr[i][j] >= 0 and i + 1 < floor: # 벽돌만, 기준 바닥보다 한칸 이상 위에 있다면.
                arr[floor - 1][j] = arr[i][j] # 기준 바닥 한칸 위로 위치 이동
                arr[i][j] = -2 # 빈공간으로 변경
                floor -= 1 # 기준바닥 한칸 위로 변경
            elif arr[i][j] > -2: # 빈공간이 아니라면. 빈공간(-2), 벽(-1), 벽돌(0 이상)
                floor = i # 기준 바닥 변경.


def Rotate():
    global arr
    arr = list(reversed(list(map(list, zip(*arr))))) # Transpose -> reversed == -90도


N, M = map(int, input().split())
arr = [[-1] * (N + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N + 2)] # -1 padding. padding을 하면 범위 조건 생략 가. 추가 입력이 없고 함수에 의해 내부적으로 값 변환만 있다면 사용 가능.
score = 0
block_group = Find_block()
while len(block_group) > 1: # 그룹 형성되었을 경우만 계산.
    score += len(block_group) ** 2
    for i, j in block_group:
        arr[i][j] = -2 # 무시 flag

    Gravity() # 중력
    Rotate() # 90도 반시계 방향으로 회전
    Gravity() # 중력
    block_group = Find_block()

print(score)