# DFS, Brute force

# - 현재 위치 청소
# - 현재 방향 기준
#   - 왼쪽 청소 여부 확인
#   - 미청소시
#       - 왼쪽 방향 회전
#       - 한칸 전진
#       - 청소
#   - 청소 완료시
#       - 왼쪽 청소 반복
#   - 4방향 모두 청소 완료 or 벽
#       - 후진 할 수 있는 경우
#           - 방향 유지
#           - 한칸 후진
#           - 왼쪽 청소 반복
#       - 후진 할 수 없는 경우(벽)
#           - 작동 정지

# 왼쪽 방향 회전
# d = (d+3) % 4
# 4방향이 0, 1, 2, 3. 왼쪽으로 돌리면 3, 2, 1, 0.

n, m = map(int, input().split())
cur = list(map(int, input().split())) # 시작 위치
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0
def DFS(y, x, d):
    global cnt
    if arr[y][x] == 0:
        cnt += 1 #
        arr[y][x] = 2 # 청소
    for _ in range(4): # 입력 d 값에 따라 순서 결정
        nd = (d+3)%4 # 왼쪽 방향 회전
        ny = y+dy[nd]
        nx = x+dx[nd]
        if arr[ny][nx] == 0: # 청소 대상
            DFS(ny, nx, nd) # 새방향, 새위치에서 DFS
            return
        d = nd
    nd = (d+2)%4 # 4방향 종료 후 뒤로 진행
    ny = y+dy[nd]
    nx = x+dx[nd]
    if arr[ny][nx] == 1: # 벽
        return
    DFS(ny, nx, d) # 뒤로 오기 전 방향 유지하여 DFS
DFS(cur[0], cur[1], cur[2])
print(cnt)