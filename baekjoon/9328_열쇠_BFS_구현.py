'''
[설명]
문서의 위치 -> 방문한 문서 위치 별도 관리(중복 방문 제한)
빌딩의 문은 모두 잠겨있기 때문에, 문을 열려면 열쇠가 필요 -> 문/열쇠 dict
상근이는 일부 열쇠를 이미 가지고 있고,
일부 열쇠는 빌딩의 바닥
상근이는 상하좌우로만 이동 -> BFS
1. '.'는 빈 공간
2. '*'는 벽을 나타내며, 상근이는 벽을 통과할 수 없음
3. '$'는 상근이가 훔쳐야하는 문서
대문자는 문 -> ord(), chr() 활용
소문자는 열쇠
마지막 줄에는 상근이가 이미 가지고 있는 열쇠
열쇠를 하나도 가지고 있지 않는 경우에는 "0"
상근이는 처음에는 빌딩의 밖에 있으며,
빌딩 가장자리의 벽이 아닌 곳을 통해 빌딩 안팎을 드나들 수 있다.-> '.' 패딩을 통해 이동 공간 확보
문을 열 수 있는 열쇠의 개수는 0개, 1개, 또는 그 이상 -> set() 관리
열쇠로 열 수 있는 문의 개수도 0개, 1개, 또는 그 이상
열쇠는 여러 번 사용

[문제]
상근이가 훔칠 수 있는 문서의 최대 개수를 출력 -> 최소가 아님. 키를 찾을 때 마다 visited 초기화 및 재탐색.
'''
'''
[알고리즘]
- 키관리 set() -> dict() 불필요
- 방문한 문서 위치 관리 list()
- 외부로 이동 가능하기 때문에, padding 필요.
- 목적이 최대 문서 개수이므로, (출발지(입구), 문 정보) 저장 불필요.
- dxy 제한 없음
- BFS
    - visited(arr 동일 크기)
    - 최소 거리가 아니고, 최대 개수이기 때문에, key를 찾을 때 마다 visited 초기화 및 재탐색.
'''
'''
[구조]
- arr 저장 + padding
- key = set()
- 초기 보유 key 저장
- 방문 문서 위치 관리 doc_loc = list()
- BFS
    - visited(arr 동일 사이즈)
    - while queue
        - nxy += dxy
        - 제한 조건: 범위 밖, 벽, 이미 방문했다면 무시
        - if 대문자 문:
            - chr(ord(+32)) not in key_list 무시
        - elif 소문자 키:
            - 키 not in key_list
                - 키 추가
                - visited 초기화
        - elif 비밀문서 and not in visited_doc:
            - visited_doc 추가
        - 방문처리
        - queue 추가
        
'''


from collections import deque

dy = [-1, 0, 1, 0]  # 상 우 하 좌
dx = [0, 1, 0, -1]  # 상 우 하 좌

def BFS():
    global ans

    queue = deque([[0, 0]])
    visited = [[False] * (W + 2) for _ in range(H + 2)] # arr 동일 사이즈
    visited[0][0] = True
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0<=nx<W+2) or not (0<=ny<H+2) or arr[ny][nx] == '*' or visited[ny][nx]: # 제한 조건: 범위 밖, 벽, 이미 방문했다면 무시
                continue

            if 'A' <= arr[ny][nx] <= 'Z':  # 대문자(문)
                if chr(ord(arr[ny][nx]) + 32) not in key:  # 해당 문을 열 수있는 키가 없다면, 무시
                    continue
            elif 'a' <= arr[ny][nx] <= 'z':  # 소문자(키)
                if arr[ny][nx] not in key:  # 아직 키에 없다면
                    key.add(arr[ny][nx])  # 키 추가
                    visited = [[False] * (W + 2) for _ in range(H + 2)]  # 키 찾으면, 새롭게 방문 체크 초기화
            elif arr[ny][nx] == "$" and (ny, nx) not in visited_doc:  # 비밀 문서, 문서 리스트에 없음
                ans += 1  # 찾은 개수 1개 증가
                visited_doc.append((ny, nx))  # 중복 방문 차단을 위한 저장

            visited[ny][nx] = True  # 방문 처리
            queue.append([ny, nx])  # 다음 위치를 큐에 삽입


T = int(input())

for _ in range(1, T + 1):
    H, W = map(int, input().split()) # 높이와 너비 h와 w (2 ≤ h, w ≤ 100)

    arr = ['.' + input() + '.' for _ in range(H)] # 양 옆 빈공간 '.' padding
    arr = ['.' * (W + 2)] + arr + ['.' * (W + 2)] # 위, 아래 빈공간 '.' padding

    key = set()  # 가지고 있는 키 저장
    visited_doc = []  # 방문한 비밀 문서 위치 저장

    for i in input(): # 초기 보유 키
        if i.isalpha(): # 알파벳 확인
            key.add(i) # 키로 저장

    ans = 0
    BFS()
    print(ans)