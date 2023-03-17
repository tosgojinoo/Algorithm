'''
[설명]
N개의 세로선과 M개의 가로선
인접한 세로선 사이에는 가로선을 놓을 수 있는데,
각각의 세로선마다 가로선을 놓을 수 있는 위치의 개수는 H이고,
모든 세로선이 같은 위치를 갖는다.

두 가로선이 연속하거나 서로 접하면 안 된다.
가로선은 점선 위에 있어야 한다.

세로선의 가장 위에서부터 아래 방향으로 내려가야 한다.
가로선을 만나면 가로선을 이용해 옆 세로선으로 이동한 다음,
이동한 세로선에서 아래 방향으로 이동

가장 위에 있는 점선의 번호는 1번이고, 아래로 내려갈 때마다 1이 증가
입력으로 주어지는 가로선이 서로 연속하는 경우는 없음

[문제]
i번 세로선의 결과가 i번이 나오도록 -> 경우의 수 DFS
추가해야 하는 가로선 개수의 최솟값 -> 경우의 수 중 결과의 최소
정답이 3보다 큰 값이면 -1
불가능한 경우에도 -1

'''
'''
[알고리즘]
- arr
    - idx shift +1 적용
    - value == 현 위치에서 연결된 선으로 향하는 열 값
- visited
    - 가로선의 도착 열 표시
    - 원위치 가능 여부 판단 위한 odd 계산 참고용
- DFS
    - odd
        - 시작점을 제외하고, visited 짝수는 원위치가 가능하다는 의미
        - 잔여 가능 횟수(최대값3 - 이미 이동 cnt) < 홀수번 방문 지점수 == 복귀 불가
    - x행 선택 > for 열 선택 > 사다리 놓기 > 방문 처리 > DFS(cnt+1, x) > 복원  
- check
    - 모든 출발열과 도착열이 동일한지 확인
    - 출발열 저장 > 행 증가하며 열 값 update > 도착열과 출발열 비교 > 다르면 False 
        
'''
'''
[구조]
- arr 설정
- visited 설정
# 가로선의 정보는 두 정수 a과 b
# b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미
- for range(M):
    - arr[y][x], arr[y][x+1] = x+1, x
    - visited[x+1] += 1

- ans = 4 # 추가해야 하는 가로선 개수 제한. 3보다 크면 -1
- DFS(0, 1) # (cnt, x)

# 문제 조건
- if ans > 3: print(-1)
- else: print(ans)


- DFS(cnt, x):
    # (문제) 제한 조건
    - if cnt 가 현재 ans 이상: return
    # (문제) 종료 조건
    - elif check(arr): # i에서 출발해서 i로 도착했는지 확인.
        - ans = min(ans, cnt)
        - return

    # (추가) 중단 조건
    - for visited:
        - if v % 2:
            - odd += 1 # 홀수번 방문한 지점 cnt
    - if odd > 3-cnt:
        - return

    # 탐색
    - for i in range(x, H+1): # 범위 주의. x 부터.
        - for j in range(1, N):
            - if 두 지점 모두 이전에 연결된 적이 없음:
                - arr[i][j], arr[i][j+1] = j+1, j # 연결 저장
                - visited[j+1] 방문처리
                - DFS(cnt+1, i)
                - arr[i][j], arr[i][j+1] = 0 복원
                - visited[j+1] 복원

    
- check(arr): # 모든 출발열과 도착열이 동일한지 확인
    - for range(1, N+1): # 세로줄
        - now = v_idx
        - for range(1, H+1): # 가로줄
            - if arr[h_idx][now]: # 값이 있다 == 연결됨
                - now = arr[h_idx][now] # 이동. 현재 열 값 update
        - if now != v_idx: # 출발(v_idx), 종료(now) 비교
            - return False
    - return True

'''


import sys
input = sys.stdin.readline

def check(arr):
    for v_idx in range(1, N+1): # 세로줄
        now = v_idx
        for h_idx in range(1, H+1): # 가로줄
            if arr[h_idx][now]: # 값이 있다 == 연결되어 있다.
                now = arr[h_idx][now] # 연결된 곳으로 이동. 이후 updated 된 열 값으로 확인
        if now != v_idx: # 출발(v_idx)와 탐색을 마쳤을때의 idx(now)가 동일하지 않으면, 문제 요구사항(i출발, i도착) unmet.
            return False
    return True


def DFS(cnt, x):
    global ans, arr
    # 제한 조건
    if cnt >= ans: # 4회 미만으로 제한
        return
    # 종료 조건
    elif check(arr): # i에서 출발해서 i로 도착했는지 확인.
        ans = min(ans, cnt)
        return

    # 중단 조건
    odd = 0
    for v in visited:
        if v % 2:
            odd += 1 # 홀수번 방문한 지점 cnt
    if odd > 3-cnt: # 짝수번 방문해야 원위치 가능한데, 홀수번 방문 지점수가 잔여 가능 횟수(최대값3 - 이미 이동 cnt)를 넘어서면 탐색 중단.
        return

    # 탐색
    for i in range(x, H+1): # 범위 주의. x 부터.
        for j in range(1, N):
            if not arr[i][j] and not arr[i][j+1]: # 두 지점 모두 이전에 연결된 적이 없다면.
                arr[i][j], arr[i][j+1] = j+1, j # 연결 관계 저장. 각 node 가 향하는 nnode.
                visited[j+1] += 1
                DFS(cnt+1, i)
                arr[i][j], arr[i][j+1] = 0, 0
                visited[j+1] -= 1

# 세로선 개수. 가로선 개수. 놓을 수 있는 위치 개수.
# (2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H)
N, M, H = map(int, input().split())

arr = [[0]*(N+1) for _ in range(H+1)] # idx 1 shift
visited = [0 for _ in range(N+1)] # 가로선의 도착 열을 표시
# 가로선의 정보는 두 정수 a과 b
# (1 ≤ a ≤ H, 1 ≤ b ≤ N-1)
# b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미
for _ in range(M):
    y, x = map(int, input().split()) # 가로선 정보
    arr[y][x], arr[y][x+1] = x+1, x # value == 현 위치에서 향하는 열값
    visited[x+1] += 1

ans = 4 # 추가해야 하는 가로선 개수 제한. 3보다 크면 -1
DFS(0, 1) # (cnt, x)

if ans > 3: # 문제 조건
    print(-1)
else:
    print(ans)