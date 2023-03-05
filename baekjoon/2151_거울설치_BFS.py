'''
[설명]
문 두개
한 쪽 문에서 다른 쪽 문 볼 수 있도록
45도 기울어진 대각선 방향으로 설치
양 쪽 모두에서 반사

[문제]
설치 최소 거울 개수
'''
'''
[알고리즘]
- 문 둘 중에 한개 선택
    - 한 곳에서 다른 한 곳을 가기만 하면 되기 때문
    - 하나 선택 -> 개별 저장 -> 빈곳'.' 처리
- dxy 조건 없음
- BFS
    - queue
        - 시작점에서 방향이 정해지지 않았음
        - 4방향에 대한 모든 경우를 queue 추가
    - while queue
        - while 이동 
            - 벽 or 밖 만나기 전까지 계속 이동
            - 종료조건: 출구
        - for nd in range(4)
            - nd != d 일때만 queue 추가
            - 이후 visited에 의해 nd =- -d 도 제외됨 
'''
'''
[구조]
- arr 입력
- door 두개 정보 추출
- door 한개 개별 저장, arr에서 삭제.
- BFS
    - visited
    - queue
    - while queue
        - queue.popleft()
        - dxy
        - while 범위내 & 벽 아님 (제한조건 포함됨)
            - x/y += dxy
            - 종료 조건: 출구
                - return cost
            - 거울 설치 위치 or 미방문
                - 방문 처리
                - 4 방향 중 이전 방향 d와 다른 경우
                    - queue 추가, (cost+1, x, y, nd)

    

'''


from collections import deque

def BFS():
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    for d in range(4): # 4방향 입력
        queue.append((0, inx, iny, d))

    while queue:
        cost, x, y, d = queue.popleft()
        dx, dy = direction[d]

        while 0<=x+dx<=N-1 and 0<=y+dy<=N-1 and arr[x+dx][y+dy] != '*': # 이동 가능할 때(벽 or 밖)까지 이동
            x += dx
            y += dy
            if arr[x][y] == '#': # 종료 조건: 출구
                return cost
            elif arr[x][y] == '!' and not visited[x][y]:
                visited[x][y] = 1
                for nd in range(4):
                    if d != nd:
                        queue.append((cost+1, x, y, nd))

N = int(input()) # 집 크기 N
Door = []
arr = [list(input()) for _ in range(N)] # 집 정보
for i in range(N):
    for j in range(N):
        if arr[i][j] == '#': 
            Door.append((i, j))
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
inx, iny = Door[0] # 문 둘중 하나만 선택
arr[inx][iny] = '.'

print(BFS())


