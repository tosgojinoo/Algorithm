import sys
input = sys.stdin.readline

def check(arr):
    for v_idx in range(1, N+1): # 세로줄
        now = v_idx
        for h_idx in range(1, H+1): # 가로줄
            if arr[h_idx][now]: # 값이 있다 == 연결되어 있다.
                now = arr[h_idx][now] # 연결된 곳으로 이동. 이후 updqted 된 열 값으로 확인
        if now != v_idx: # 출발(v_idx)와 탐색을 마쳤을때의 idx(now)가 동일하지 않으면, 문제 요구사항(i출발, i도착) unmet.
            return False
    return True


def DFS(count, x):
    global ans, arr
    # 제한 조건
    if count >= ans: # 4회 미만으로 제한
        return
    # 종료 조건
    elif check(arr): # i에서 출발해서 i로 도착했는지 확인.
        ans = min(ans, count)
        return

    # 중단 조건
    odd = 0
    for v in visited:
        if v % 2:
            odd += 1 # 홀수번 방문한 지점 cnt
    if odd > 3-count: # 짝수번 방문해야 원위치 가능한데, 홀수번 방문 지점수가 잔여 가능 횟수(최대값3 - 이미 이동 cnt)를 넘어서면 탐색 중단.
        return

    # 탐색
    for i in range(x, H+1): # 범위 주의. x 부터.
        for j in range(1, N):
            if not arr[i][j] and not arr[i][j+1]: # 두 지점 모두 이전에 연결된 적이 없다면.
                arr[i][j], arr[i][j+1] = j+1, j # 연결 관계 저장. 각 node 가 향하는 nnode.
                visited[j+1] += 1
                DFS(count+1, i)
                arr[i][j], arr[i][j+1] = 0, 0
                visited[j+1] -= 1


N, M, H = map(int, input().split()) # 세로, 놓을 수 있는 개수, 가로.
arr = [[0]*(N+1) for _ in range(H+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    y, x = map(int, input().split()) # 가로선 정보
    arr[y][x], arr[y][x+1] = x+1, x
    visited[x+1] += 1


ans = 4 # 추가해야 하는 가로선 개수 제한. 3보다 크면 -1
DFS(0, 1) # (count, x)

if ans > 3: # 문제 조건
    print(-1)
else:
    print(ans)