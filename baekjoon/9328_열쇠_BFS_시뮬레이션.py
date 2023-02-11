'''my idea
문 정보 관리 door_info = {문 알파벳: (y,x)}
키 정보 관리 key_info = set()
입구 정보 관리 entrance = set()

for 입구 정보
  - DFS
  - 키(소문자)를 만날 경우
      - key_info.add(key)
      - if key in door_info.keys()
          - 문으로 이동
          - door_info 에서 문 삭제
          - visited가 0인 곳으로 이동
  - if $ 만날 경우
      - cnt += 1
cnt 출력
'''
'''
- 키 정보 관리 key = set()
- 방문한 문서 위치 관리(재방문 차단) visited_doc = []
- ***  키 찾으면, visited 초기화
- ***  비밀문서 위치 저장하여, 중복 방문 차단
'''


from collections import deque

dy = [-1, 0, 1, 0]  # 상 우 하 좌
dx = [0, 1, 0, -1]  # 상 우 하 좌

def BFS():
    global ans

    queue = deque([[0, 0]])
    visited = [[False] * (W + 2) for _ in range(H + 2)]
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
    H, W = map(int, input().split())

    # pedding
    arr = ['.' + input() + '.' for _ in range(H)] # 양 옆
    arr = ['.' * (W + 2)] + arr + ['.' * (W + 2)] # 위, 아래

    key = set()  # 가지고 있는 키 저장
    visited_doc = []  # 방문한 비밀 문서 위치 저장

    for i in input():
        if i.isalpha():  # 알파벳 확인
            key.add(i)  # 키로 저장

    ans = 0
    BFS()
    print(ans)