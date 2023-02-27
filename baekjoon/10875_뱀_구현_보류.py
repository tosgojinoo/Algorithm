def solve():
    ans = 1
    flag = False # 충돌
    x, y, direction = L, L, 0 # 시작은 중앙, 오른쪽 방향. idx는 0부터 시작, 0에서 L번 이동이 중앙.
    for t, d in cmd:
        if direction % 2 == 0: # 수평 방향
            temp = float('inf')
            nx = x + dx[direction] * t
            minX, maxX = min(x, nx), max(x, nx) # x, nx 중 크고 작은 값 각각 저장
            for a, b, c in hori[:-1]: # (minY, maxY, x). [(0, N, -1), (0, N, N), (L, L, L)]
                if a <= y <= b and minX <= c <= maxX: # 크로스 여부 확인
                    flag = True
                    temp = min(abs(c - x) - 1, temp) # 충돌 전까지 이동 가능 거리
            if flag: # 충돌. 결과 출력
                return ans + temp
            else: # 충돌 x. 결과 누적.
                ans += t
                x = nx
                vert.append((minX, maxX, y)) # 직선의 위치(시작, 끝, 수평 위치) 저장
        else: # 수직 방향
            temp = float('inf')
            ny = y + dy[direction] * t
            minY, maxY = min(y, ny), max(y, ny)
            for a, b, c in vert[:-1]: # (minX, maxX, y). [(0, N, -1), (0, N, N)]
                if a <= x <= b and minY <= c <= maxY: # 크로스 여부 확인
                    flag = True
                    temp = min(abs(c - y) - 1, temp)
            if flag:
                return ans + temp
            else:
                ans += t
                y = ny
                hori.append((minY, maxY, x)) # 직선의 위치(시작, 끝, 수직 위치) 저장
        direction = (direction + d) % 4
    return ans

L = int(input())
N = 2 * L + 1 # 최대 폭
cmd = []
dirs = {'L':-1, 'R':1}
for _ in range(int(input())):
    t, d = input().split()
    cmd.append((int(t), dirs[d]))
cmd.append((N, 0))
print(cmd)
vert = [(0, N, -1), (0, N, N)] # (minX, maxX, y)
hori = [(0, N, -1), (0, N, N), (L, L, L)] # (minY, maxY, x). (L, L, L) 은 무효값
dx = [1, 0, -1, 0] # 오, 하, 왼, 상
dy = [0, 1, 0, -1]

print(solve())