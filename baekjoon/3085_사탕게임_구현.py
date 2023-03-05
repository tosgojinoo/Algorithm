'''
[설명]

[문제]
'''
'''
[알고리즘]

'''
'''
[구조]

'''

# (N-1) x (N-1) 요소 탐색
# case: 색 교환x, 해당 요소와 인접 두 곳(우, 아래)과 색 교환
#   - 각각의 경우에 4방향 DFS
#       - 시작 방향 지정 및 유지되는 DFS
#       - 시작 요소와 다른 색일 경우 종료
#       - cnt = level
#       - visited[status(색교환0~2)][y][x]
# max(visited) 출력

# 최대 개수 세기
def check(arr):
    res = 0
    for y in range(N):
        cnt = 1 # 자기 자신
        for x in range(N):
            if arr[y][x] == arr[y][x+1]: # 같은 색일 경우. 오른쪽 방향
                cnt += 1
            else: # 아니면 리셋
                cnt = 1
            res = max(res, cnt)
        cnt = 1
        for x in range(N):
            if arr[x][y] == arr[x+1][y]: # 같은 색일 경우. 아래 방향
                cnt += 1
            else: # 아니면 리셋
                cnt = 1
            res = max(res, cnt)
    return res


N = int(input())
arr = [list(input()) for _ in range(N)]
ans = 1

for y in range(N):
    for x in range(N):
        if x < N - 1:
            arr[y][x], arr[y][x + 1] = arr[y][x + 1], arr[y][x] # 두 색 교환
            ans = max(ans, check(arr))
            arr[y][x], arr[y][x + 1] = arr[y][x + 1], arr[y][x] # 원복

        if y < N - 1:
            arr[y][x], arr[y + 1][x] = arr[y + 1][x], arr[y][x] # 두 색 교환
            ans = max(ans, check(arr))
            arr[y][x], arr[y + 1][x] = arr[y + 1][x], arr[y][x] # 원복
print(ans)