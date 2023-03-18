'''
[설명]
N×N
블록은 검은색 블록, 무지개 블록, 일반 블록
일반 블록은 M가지 색상
색은 M이하의 자연수
검은색 블록은 -1, 무지개 블록은 0
(i, j)는 격자의 i번 행, j번 열
|r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸 (r1, c1)과 (r2, c2)를 인접한 칸

- 그룹 조건
    - 블록 그룹은 연결된 블록의 집합
    - 그룹에는 일반 블록이 적어도 하나
    - 일반 블록의 색 동일
    - 검은색 블록은 불포함
    - 무지개 블록은 얼마나 들어있든 상관없음
    - 그룹에 속한 블록의 개수는 2보다 크거나 같음
    - 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동 가능
    - 블록 그룹의 기준 블록
        - 무지개 블록이 아닌 블록 중
            - 행의 번호가 가장 작은 블록
                - 열의 번호가 가장 작은 블록

- 오토 플레이
    - 블록 그룹이 존재하는 동안 계속해서 반복
    [우선순위]
    - 크기가 가장 큰 블록 그룹을 찾음 -> find_block()
        - 포함된 무지개 블록의 수가 가장 많은 블록 그룹
            - 행이 가장 큰 것
                - 열이 가장 큰 것
    - 찾은 블록 그룹의 모든 블록 제거
        - 블록의 수를 B라고 했을 때, B^2 점
    - 격자에 중력 작용
        - 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동
        - 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속
    - 격자가 90도 반시계 방향 회전
    - 격자에 중력 작용


[문제]
획득한 점수의 합
'''
'''
[알고리즘]
- arr: 외곽에 -1 padding으로 범위 조건 생략.
- find_block()
    - BFS 미사용
    - 조건에 맞으면 queue 추가 & 추가가 없을 때까지 탐색
    - deque가 아닌 단순 list queue 
    - 길이 조건과 idx 증가를 복합 사용
    - while block_idx < len(queue): 
        - block_idx ++
    - max_block
        - 우선순위 조건이 많음 & 배열 내용도 함께 참고해야할 때
        - tuple로 한번에 묶어 활용 가능
        - max(max_block, (len(queue), len(rainbow), i, j, queue)) 
- 탐색
    - 이미 처리되어 더이상 방문할 필요 없을 경우, 시간 절약을 위해 
    - visited 방문처리 되었지만
    - 추가로 arr에 flag 처리 필요
    - 이 문제에서는 삭제 과정이 있기 때문에, 빈공간 flag -2 적용
- Gravity()
    - 중력 처리시
    - 열 순서
        - 기준선 설정 (중력 정렬 완료 지점, 이하는 빈공간 없음)
        - 행 역순, 마지막줄 제외
            - 기준선 위로 블록 위치 변경
            - or 기준선 위치 이동
- Rotate()
    - +90도
        - transpose > -c
    - -90도
        - transpose > reverse
        - reversed(list(map(list, zip(*arr))))
    - 180도
        - (y, x) -> (-y, x) or (y, -x)
'''
'''
[구조]
# 블록 정보. -1, 0, M 이하 자연수
- arr 저장. 외곽에 -1 padding. padding으로 범위 조건 생략.
- block_group = Find_block()
- while 블록 그룹 형성 되었을 경우: 
    - score += len(block_group) ** 2
    - for block_group:
        - arr[i][j] = -2 # 탐색 제외 flag

    - Gravity() 중력
    - Rotate() 90도 반시계 방향 회전
    - Gravity() 중력
    - block_group = Find_block()

- print(score)


- Find_block():
    - visited = arr 동일 크기. 외곽은 -1 padding.
    # max 우선순위: 가장 큰 블록(len(queue) > 가장 많은 무지개(len(rainbow)) > 기준 행값 > 기준 열값. 마지막에 queue를 함께 저장해 전달.
    - max_block = (0, 0, 0, 0, []) 

    - for 전체 탐색하며:
        - if 방문 했거나, arr == 0(무지개 블록): 무시

        - block_num 확인
        - visited[si][sj] 방문처리
        - queue = [(si, sj)] # 거쳐간 데이터들 재사용 할 것이기 때문에, not deque.
        - rainbow = []
        - block_idx = 0. queue 탐색용
        - while block_idx < len(queue): # 조건에 맞으면 queue 추가 & 추가가 없을 때까지 탐색 
            - block_idx ++
            - for 4방:
                - if 미방문:
                    - if 무지개 블록:
                        - visited[ni][nj] 방문처리
                        - rainbow 추가
                        - queue 추가
                    - elif 동일 블록 숫자:
                        - visited[ni][nj] 방문처리
                        - queue 추가
        # max 우선순위: 가장 큰 블록(len(queue) > 가장 많은 무지개(len(rainbow)) > 기준 행값 > 기준 열값. 마지막에 queue를 함께 저장해 전달.
        - max_block = max(max_block, (len(queue), len(rainbow), si, sj, queue)) 

        - for rainbow: 
            - visited[i][j] 초기화

    - return max_block[-1]

- Gravity():
    - for 열 순서대로: 
        - floor = N + 1 # 정렬 기준선 선정
        - for 행 역순, 맨 아래줄(N+1)은 제외:
            - if 벽돌만, 기준선보다 한칸 이상 위에 있다면: 
                - 기준선 한칸 위로 벽돌 위치 이동
                - 기존 위치 빈공간으로 변경
                - floor -- 기준선의 위치 이동
            - elif 빈공간이 아니라면:
                - floor = i 기준선 위치 이동

- Rotate():
    # Transpose -> reversed == -90도
    - arr = list(reversed(list(map(list, zip(*arr)))))

'''

def Find_block():
    visited = [[arr[i][j] < 0 for j in range(N + 2)] for i in range(N + 2)] # -1 벽은 True 방문 처리
    max_block = (0, 0, 0, 0, []) # max 우선순위: 가장 큰 블록(len(queue) > 가장 많은 무지개(len(rainbow)) > 기준 행값 > 기준 열값. 마지막에 queue를 함께 저장해 전달.

    for si in range(1, N + 1):
        for sj in range(1, N + 1): # 전체 탐색하며, 계산 대상 선정
            if visited[si][sj] or not arr[si][sj]: # 방문 했거나, arr == 0(무지개 블록) 이면 무시.
                continue

            block_num = arr[si][sj]
            visited[si][sj] = True
            queue = [(si, sj)] # 거쳐간 데이터들 재사용 할 것이기 때문에, not deque.
            rainbow = []
            block_idx = 0
            while block_idx < len(queue):
                i, j = queue[block_idx]
                block_idx += 1
                for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if not visited[ni][nj]: # 미방문
                        if not arr[ni][nj]: # 무지개 블록
                            visited[ni][nj] = True # 방문처리
                            rainbow.append((ni, nj))
                            queue.append((ni, nj))
                        elif arr[ni][nj] == block_num: # 동일 블록 숫자
                            visited[ni][nj] = True
                            queue.append((ni, nj))

            max_block = max(max_block, (len(queue), len(rainbow), si, sj, queue)) # max 우선순위: 가장 큰 블록(len(queue) > 가장 많은 무지개(len(rainbow)) > 기준 행값 > 기준 열값. 마지막에 queue를 함께 저장해 전달.

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


N, M = map(int, input().split()) # 격자 한 변의 크기 N, 색상의 개수 M
# 블록 정보
# -1, 0, M 이하 자연수
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