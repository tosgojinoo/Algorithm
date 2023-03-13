'''
[설명]
N×N
(r, c)는 격자의 r행 c열
A[r][c]는 (r, c)에 있는 모래의 양

격자의 가운데 칸부터 토네이도의 이동이 시작
토네이도는 (1, 1)까지 이동한 뒤 소멸
토네이도는 한 번에 한 칸 이동

- 모래 이동
    - 토네이도가 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 퍼짐
    - 토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동
    - 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다. -> y * 비율만큼 정해진 칸에 퍼짐
    - α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양
    - 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해짐
    - 비율은 해당 방향으로 회전 적용
    - 모래가 격자의 밖으로 이동 가능

[문제]
격자의 밖으로 나간 모래의 양
'''
'''
[알고리즘]
- 방향별 모래 비율
    - 우선, 문제에 제시된 왼쪽 방향으로 좌표 및 비율을 리스트 저장
        - [(상대좌표 r/c, 비율)]
    - 토네이도 이동 방향에 따라 개별 정의. 좌표만 변경.
        - 오른쪽: y -> -y
        - 아래: x -> y, y -> -x
        - 위: x -> y, y -> x
    - 잔여 비율 a는 0으로 초기값 설정
        - 이후, 누적 total 계산해 빼줘 적용
        - 소수점 버림(int) 계산 때문
- 토네이도 이동
    - step 을 1~N까지 증가시키면서
    - 좌/하, 우/상 묶음으로 recount() 적용하면
    - arr 전체 이동을 만족하게 됨
    - step
        - 홀수 일 때: 좌/하
        - 짝수 일 때: 우/상
'''
'''
[구조]
- arr 모래 양 저장
- left = [(1, 1, 0.01), (-1, 1, 0.01),
          (1, 0, 0.07), (-1, 0, 0.07),
          (1, -1, 0.1), (-1, -1, 0.1),
          (2, 0, 0.02), (-2, 0, 0.02),
          (0, -2, 0.05), (0, -1, 0)]
- right = [(x, -y, z) for x, y, z in left]
- down = [(-y, x, z) for x, y, z in left]
- up = [(y, x, z) for x, y, z in left]

- 시작좌표 설정. arr 중심.
- ans = 0  # 범위 밖 나간 양 저장용

(토네이도 회전 방향)
- for step (1 ~ N):
    - if 홀수 step:
        - recount(step, 0, -1, left) # (step, 방향 dxy, 방향에 따른 비율 array)
        - recount(step, 1, 0, down)
    - else 짝수: 
        - recount(step, 0, 1, right)
        - recount(step, -1, 0, up)

- print(ans)

- recount(time, dx, dy, direction):
    # y좌표 계산 & x좌표 갱신
    - for time 만큼 반복:
        - 시작 좌표에 dxy ++
        - if y가 범위 밖이면: 중지 (회전하다 마지막을 넘어서면 y값(col_idx)만 먼저 벗어남)
        - 잔여 비율 a 구하기 위한 변수 설정
        - for 비율 array에서 하나씩 확인:
            - if 비율:
                - new_arr = 비율만큼 분배
                - total에 누적
            - else 잔여 비율 a(초기값은 0): 
                - new_arr = 모래 초기값 - total

            - if 범위 내:
                - arr[nx][ny] += new_arr
            - else 범위 밖:  
                - ans += new_arr
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
            if weight: # 비율
                new_arr = int(arr[s_x][s_y] * weight)
                total += new_arr
            else: # 잔여 비율 a
                new_arr = arr[s_x][s_y] - total # 계산 중 int 처리로 인해, 누적값을 따로 계산 후 직접 빼줘야함

            if 0 <= nx < N and 0 <= ny < N:   # 범위내 이면 값 갱신
                arr[nx][ny] += new_arr
            else:  # 범위 밖이면 ans 추가
                ans += new_arr


N = int(input()) # 격자크기 N
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

s_x, s_y = N//2, N//2  # 시작좌표. arr 중심.
ans = 0  # out_arr

# 1.토네이도 회전 방향(y위치)
for step in range(1, N + 1):
    if step % 2: # 홀수
        recount(step, 0, -1, left) # (time, dx, dy, direction)
        recount(step, 1, 0, down)
    else: # 짝수
        recount(step, 0, 1, right)
        recount(step, -1, 0, up)

print(ans)