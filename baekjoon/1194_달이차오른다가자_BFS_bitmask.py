'''
[설명]
미로는 직사각형 모양이고, 여행길을 떠나기 위해 미로를 탈출
- 빈 칸: 언제나 이동할 수 있다. ('.')
- 벽: 절대 이동할 수 없다. ('#')
- 열쇠: 언제나 이동할 수 있다. 이 곳에 처음 들어가면 열쇠를 집는다. ('a', 'b', 'c', 'd', 'e', 'f') -> 키 보유 상태에 따라 구분됨. bitmask. visited 반영. 추가 memory 리스트 구성.
- 문: 대응하는 열쇠가 있을 때만 이동할 수 있다. ('A', 'B', 'C', 'D', 'E', 'F') -> ord() 사용. 알파벳 내 idx 계산. 보유 키와 bit 연산.
- 민식이의 현재 위치: 빈 곳이고, 민식이가 현재 서 있는 곳이다. ('0') -> 이후 영향 없으므로, 따로 저장 후 빈칸 초기화
- 출구: 달이 차오르기 때문에, 민식이가 가야하는 곳이다. 이 곳에 오면 미로를 탈출한다. ('1')
한 번의 움직임은 현재 위치에서 수평이나 수직으로 한 칸 이동

[문제]
첫째 줄에 민식이가 미로를 탈출하는데 드는 이동 횟수의 최솟값 출력 -> 이동 횟수 최소값, BFS
미로를 탈출 할 수 없으면, -1을 출력.
'''
'''
[알고리즘]
- dxy 생성 제한 없음
- 민식이 초기 위치는 전체 탐색에 영향 없음 -> 제거('.') 후 start에 저장.
- BFS
    - visited[x][y][2**len("abcdef")]
        - 갖고 있는 키 상태에 따라 구분 -> bitmask
        - BOJ 9328_열쇠와 다르게, key 개수가 정해져 있으므로 비트마스크 활용 필수
        - 동일 키 보유 상태에서 반복 방문하면 안되기 때문에 visited에 포함 
        - 모든 곳 들이는 것이 아닌, 최단거리 도착이므로, key 확보 후 visited reset 방식 아님.
    - queue = [(x, y, cnt, key)]
        - 우선순위 없음
        - key도 분기 영향 요소
    - while queue:
        - 종료 조건: arr[x][y] == '1'. return cnt
        - 4방향 이동
            - 범위 내, 벽 아님, 동일 키 상태 일때 미방문.
                - 빈칸 '.'
                    - 방문 처리
                    - queue 추가 (nx, ny, cnt+1, key)
                - 출구 "1"
                    - 종료 조건. return cnt+1
                - 문 & 보유 키와 맞는지 확인
                    - 보유키와 비교
                        - 문(arr[nx][ny]) -> ord() -> -65 == 대문자 내 idx -> 1<<'계산값'으로 비트 변환
                        - key 비트열 & '계산값 -> 1이면 보유, 0이면 없음
                    - 방문 처리
                    - queue 추가 (nx, ny, cnt+1, key)
                - 키 & 동일 키 상태로 미방문
                    - 동일 키 상태 방문 확인
                        - 키(arr[nx][ny]) -> ord() -> -97 == 소문자 내 idx -> key|(1<<'계산값'), 추가된 키상태로 비트 갱신 -> visited idx 값 적용
                        - visited[nx][ny][key|(1 << ord(arr[nx][ny]) - 97)] 
                    - 방문 처리
                    - queue 추가 (nx, ny, cnt+1, key | (1 << ord(arr[nx][ny]) - 97), 키값 업데이트 해서 queue 저장    
    - return -1
'''
'''
[구조]
- arr 입력
- start 저장
- BFS
    - visited 
    - queue
    - while queue:
        - 종료 조건: '-1' 만남
        - 4방향 이동
            - 빈칸 '.' 
                - 방문처리, queue 추가
            - 출구 '1'
                - 종료조건, return
            - 문 '대문자' & 보유키 일치 확인
                - 방문처리, queue 추가
            - 키 '소문자' & 동일 키 상태로 이전 방문 확인
                - 방문 처리, 키 추가하여 queue 추가
'''


from collections import deque

def BFS():
    queue = deque([(start[0], start[1], 0, 0)])
    visited = [[[0] * 2**len("abcdef") for _ in range(M)] for _ in range(N)]
    visited[start[0]][start[1]][0] = True
    while queue:
        x, y, cnt, key = queue.popleft()
        if arr[x][y] == "1":
            return cnt
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] != '#' and not visited[nx][ny][key]: # 범위 내, 벽 아님, 동일 키 상태일때 미방문.
                if arr[nx][ny] == '.': # 빈칸
                    visited[nx][ny][key] = True
                    queue.append((nx, ny, cnt+1, key))
                elif arr[nx][ny] == "1": # 출구
                    return cnt+1
                elif arr[nx][ny] in "ABCDEF" and key & 1 << (ord(arr[nx][ny]) - ord('A')): # 문, 보유키와 맞는지.
                    visited[nx][ny][key] = True
                    queue.append((nx, ny, cnt+1, key))
                elif arr[nx][ny] in "abcdef" and not visited[nx][ny][key|(1 << ord(arr[nx][ny]) - ord('a'))]: # 키, 동일 키 상태로 미방문.
                    visited[nx][ny][key | (1 << ord(arr[nx][ny]) - ord('a'))] = True
                    queue.append((nx, ny, cnt+1, key | (1 << ord(arr[nx][ny]) - ord('a'))))
    return -1


N, M = map(int,input().split()) # 세로 N, 가로 M. idx 1부터.
arr = [list(input()) for _ in range(N)] # 미로 모양
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # 제한 없음
start = None
for i in range(N):
    for j in range(M):
        if arr[i][j] == "0": # 민식이 위치
            arr[i][j] = '.' # 제거
            start = (i, j) # 저장

print(BFS())