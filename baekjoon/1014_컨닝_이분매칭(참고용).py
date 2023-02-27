def bip_match(n, m): # 이분 매칭
    for nn, mm in [(n, m - 1), (n, m + 1), (n - 1, m - 1), (n - 1, m + 1), (n + 1, m - 1), (n + 1, m + 1)]: # 6방향으로 탐색
        if 0 <= nn < N and 0 <= mm < M and not visited[nn][mm] and seat[nn][mm]:
            visited[nn][mm] = True
            if connect[nn][mm] == [-1, -1] or bip_match(connect[nn][mm][0], connect[nn][mm][1]):
                connect[nn][mm] = [n, m]
                return True
    return False


# main
for tc in range(int(input())):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]
    seat = [[False] * M for _ in range(N)]  # 앉을 수 있는 자리인지 저장하기 위한 행렬
    ans = 0
    for n in range(N):
        for m in range(M):
            if arr[n][m] == '.':
                seat[n][m] = True
                ans += 1 # 앉을 수 있는 자리이면 seat 갱신해주고 answer에 자리 수 저장

    connect = [[[-1] * 2 for _ in range(M)] for __ in range(N)] # 각 자리 별 연결 위치를 저장하는 행렬
    for y in range(N):
        for x in range(0, M, 2): # 여기서 짝수로 해도 되고 홀수로 해도 된다. 물론, 둘 다 하면 안된다.
            if seat[y][x]:
                visited = [[False] * M for _ in range(N)]
                if bip_match(y, x):
                    ans -= 1 # 이분 매칭이 될 때마다 앉을 수 있는 자리가 하나씩 줄어든다

    print(ans)

