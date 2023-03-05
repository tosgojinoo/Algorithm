from collections import Counter

N = int(input())
like_list = [None] * (N ** 2) # 좋아하는 학생. 최대 명수 N**2
order = []
for _ in range(N ** 2):
    idx, a, b, c, d = map(lambda x: int(x) - 1, input().split())
    like_list[idx] = [a, b, c, d]
    order.append(idx)

blank = [[4] * N for _ in range(N)] # 인접한 빈칸수
for i in (0, N - 1):
    for j in range(N):
        if not j or j == (N - 1):
            blank[i][j] = 2
        else:
            blank[i][j] = 3
            blank[j][i] = 3
# [[2, 3, 2], [3, 4, 3], [2, 3, 2]]


seat = [None] * (N ** 2) # 학생이 앉은 자리만 저장
arr = [[False] * N for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for idx in order: # 학생 배정 순서
    like_student = like_list[idx]
    available_seat = []
    for s in like_student:
        if seat[s]: # 앉아있으면.
            y, x = seat[s]
            for dy, dx in direction: # 인근 4방 확인
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and not arr[ny][nx]: # 범위내, 빈자리
                    available_seat.append((blank[ny][nx], ny, nx)) # 추가

    if not available_seat: # 빈자리 없음
        max_blank = -1
        for i in range(N):
            for j in range(N):
                if not arr[i][j] and blank[i][j] > max_blank: # 빈자리.
                    max_blank = blank[i][j]
                    max_seat = (i, j)
                if max_blank == 4:
                    break
            if max_blank == 4: break
    else:
        available_seat = Counter(available_seat) # 빈자리 있으면, {(blank[ny][nx], ny, nx): cnt}
        available_seat = sorted(available_seat.items(), key=lambda x: (-x[1], -x[0][0], x[0][1:])) # 우선순위: 자리수 cnt > blank(인접 빈칸수) > 좌표
        max_seat = available_seat[0][0][1:] # 맨 앞조건 자리 저장

    i, j = max_seat
    arr[i][j] = idx + 1
    seat[idx] = max_seat
    for dy, dx in direction:
        ny, nx = dy + i, dx + j
        if 0 <= ny < N and 0 <= nx < N:
            blank[ny][nx] -= 1

happiness = 0
happiness_lst = [0, 1, 10, 100, 1000]
for idx, (y, x) in enumerate(seat):
    cnt = 0
    for friend in like_list[idx]:
        fy, fx = seat[friend]
        if abs(fy - y) + abs(fx - x) == 1: # 직선거리 합이 1이면.
            cnt += 1
    happiness += happiness_lst[cnt]
print(happiness)