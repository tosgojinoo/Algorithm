# (1,1) -> (5,5) 도착 가능 & 모든 곳 방문 이면 가능
# DFS 경우의 수 중 위 조건 만족하는 개수

def DFS(R, C):
    global cnt

    if R == C == 4:
        if len(visited) == 25 - K: # 못 가는 곳을 제외하고 전부 들렸는지 확인
            cnt += 1
        return

    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        newR, newC = R + dr, C + dc
        if 0 <= newR < 5 and 0 <= newC < 5 and \
                (newR, newC) not in visited and arr[newR][newC]:
            visited.add((newR, newC))
            DFS(newR, newC)
            visited.remove((newR, newC))


arr = [[1] * 5 for _ in range(5)]
visited = {(0, 0)}
cnt = 0

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    arr[i - 1][j - 1] = 0 # 방문 불가인 곳 처리

DFS(0, 0)

print(cnt)