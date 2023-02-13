# DFS, Brute force x, back tracking o
# D[i][j] 는 D[j][i]와 함께 계산
# 탐색 범위는 위삼각형 한정 <- X
# 배열로 나열, 절반이 각각 다른팀
# ***** visited 로 N명 중 선정 여부 체크. arr 에 대한 visited 아님.

def DFS(depth, idx):
    global min_diff
    if depth == N//2: # 절반만 계산. [0,1,2]가 선택되면 나머지는 자동 다른팀
        power1, power2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]: # 2명씩 확인. 선정되면 포함.
                    power1 += arr[i][j]
                elif not visited[i] and not visited[j]: # 아니면 다른팀
                    power2 += arr[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            DFS(depth+1, i+1)
            visited[i] = False


N = int(input())

visited = [False for _ in range(N)] # N 명
arr = [list(map(int, input().split())) for _ in range(N)]
min_diff = int(1e9)

DFS(0, 0)
print(min_diff)