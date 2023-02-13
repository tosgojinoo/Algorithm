'''
- move_tornado()
    - 좌 1, 하 1
    - 우 2, 상 2
    - 좌 3, 하 3
    - 우 4, 상 4
    - ...

- move_arr()
    - d 유지
    - tornado[r][c] -> tornado[r+d][c+d]
    - arr[r+d][c+d] * a -> arr[r+2d][c+2d]

(1,1)로 이동 후 소멸
격자 밖으로 이동한 모래 합계 출력

'''
# import sys
#
# input = sys.stdin.readline

# 모래 계산하는 함수
def recount(time, dx, dy, direction):
    global ans, s_x, s_y

    # y좌표 계산 & x좌표 갱신
    for _ in range(time):
        s_x += dx
        s_y += dy
        if s_y < 0: # 범위 밖이면 stop
            break

        # 3. a, out_arr
        total = 0  # a 구하기 위한 변수
        for dx, dy, weight in direction:
            nx = s_x + dx
            ny = s_y + dy
            if weight == 0:  # a(나머지). 계산 중 int 처리로 인해, 누적값을 따로 계산 후 직접 빼줘야함
                new_arr = arr[s_x][s_y] - total
            else: # 비율
                new_arr = int(arr[s_x][s_y] * weight)
                total += new_arr

            if 0 <= nx < N and 0 <= ny < N:   # 범위내 이면 값 갱신
                arr[nx][ny] += new_arr
            else:  # 범위 밖이면 ans 추가
                ans += new_arr


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 2. 방향별 모래 비율 위치
left = [(1, 1, 0.01), (-1, 1, 0.01),
        (1, 0, 0.07), (-1, 0, 0.07),
        (1, -1, 0.1), (-1, -1, 0.1),
        (2, 0, 0.02), (-2, 0, 0.02),
        (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left] # 방향별 좌표만 변경
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

s_x, s_y = N//2, N//2  # 시작좌표(x좌표). arr 중심.
ans = 0  # out_arr

# 1.토네이도 회전 방향(y위치)
for step in range(1, N + 1):
    if step % 2: # 홀수
        recount(step, 0, -1, left)
        recount(step, 1, 0, down)
    else: # 짝수
        recount(step, 0, 1, right)
        recount(step, -1, 0, up)

print(ans)