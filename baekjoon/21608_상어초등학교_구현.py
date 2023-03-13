'''
[설명]
N×N
학생 수 N^2
학생은 1번부터 N^2번까지
(r, c)는 r행 c열
교실의 가장 왼쪽 윗 칸은 (1, 1)
가장 오른쪽 아랫 칸은 (N, N)
|r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다

- 규칙
    - 비어있는 칸 중, 좋아하는 학생이 인접한 칸에 가장 많은 칸
        - 인접한 칸 중에서, 비어있는 칸이 가장 많은 칸
            - 행의 번호가 가장 작은 칸
                - 열의 번호가 가장 작은 칸
- 학생의 만족도
    - 자리 배치가 모두 끝난 후
    - 학생과 인접한 칸에 앉은 좋아하는 학생의 수
        - 0이면 학생의 만족도는 0
        - 1이면 1
        - 2이면 10
        - 3이면 100
        - 4이면 1000

[문제]
학생의 만족도의 총 합
'''
'''
[알고리즘]
- memory
    - 학생 배정 순서 order
    - 학생별 좋아하는 학생 like_list
    - 학생 앉은 자리 저장 seat
- blank
    - 인접 빈칸수 미리 계산
    - 매번 인접 빈칸을 계산하게 되면 계산량 증가함 
    - N x N 크기
    - 모서리는 2, 각 변은 3, 나머지 4
    - 진행하며 학생이 앉게 되면, 그 주위 4방의 blank 값 -1 차감
- available_seat
    - 저장은 (blank[ny][nx], ny, nx)
    - 활용
        - 중복 저장 허용으로, 중복이 많으면 이미 앉아있는 좋아하는 친구들이 많다는 의미
        - Counter로 재구성: {(blank[ny][nx], ny, nx): cnt}
        - Sort로 정렬
            - 우선순위: 자리 중족 cnt > blank(인접 빈칸수) > 좌표
            - sorted(available_seat.items(), key=lambda x: (-x[1], -x[0][0], x[0][1:]))
        - 맨 앞조건 자리 활용: available_seat[0][0][1:] (좌표만) 
'''
'''
[구조]
- blank = N x N 크기. init 4.
- for i 는 0 or (N - 1): # r 모서리
    - for j in range(N):
        - if j 가 0 or (N - 1): # c 모서리
            - blank[i][j] = 2
        - else:
            - blank[i][j] = 3
            - blank[j][i] = 3 # 대각선 반대 위치
            
- like_list = [None] * (N ** 2) # 좋아하는 학생. 최대 명수 N**2
- order = 학생 배정 순서 저장용
- for 총 학생수 (N ** 2):
    - idx, a, b, c, d = 입력. idx -1 shift 필요. 
    - like_list[idx] = [a, b, c, d] 저장
    - order.append(idx)
- seat = 학생이 앉은 자리만 저장
- arr = N x N. init False.
- direction = 4방향

- for order 학생 배정 순서: 
    - available_seat = 가능한 자리 초기화
    [우선순위 1] 좋아하는 학생이 앉아 있다면, 그 주위 빈자리
    - for 좋아하는 학생 목록:
        - if 좋아하는 학생이 앉아있으면:
            - for 앉은 자리 인근 4방:
                - if 범위내, 빈자리:
                    - available_seat 가능한 자리에 추가 (빈칸 개수 blank[ny][nx], ny, nx) -> 중복 추가. 많을 수록 좋아하는 친구들이 주위에 많음.
    
    [우선순위 2] 자신이 빈자리 & 주위 최대 빈자리
    - if not available_seat 좋아하는 학생 기준 가능한 자리 없음:  
        - max_blank = -1
        - for i in range(N):
            - for j in range(N):
                - if arr 빈자리 and 주위 빈자리 blank[i][j] > max_blank:
                    - max_blank = blank[i][j] # 주위 최대 빈자리 개수 저장
                    - max_seat = (i, j) 최대 빈자리 위치 저장
                - if max_blank == 4: # 4일 경우 최대값으로, 검색 중단. [우선순위 4] 열 변호가 작을 수록.
                    - break
            - if max_blank == 4: 4일 경우 최대값으로, 검색 중단. [우선순위 3] 행 변호가 작을 수록. 
                - break
    - else: [우선순위 1 만족]
        - available_seat = {(blank[ny][nx], ny, nx): cnt}
        - available_seat = sorted(available_seat.items(), 우선순위: 자리 중복 cnt > blank(인접 빈칸수) > 좌표)
        - max_seat = available_seat[0][0][1:] # 맨 앞조건 자리 저장

    - i, j = max_seat # 조건에 맞는 자리
    - arr[i][j] 에 학생번호 입력
    - seat에 (i, j) 저장
    - for 4방:
        - if 범위내:
            - blank[ny][nx] --
            
- happiness 행복도
- happiness_lst = [0, 1, 10, 100, 1000]
- for seat:
    - for like_list[idx]:
        - if 본인과 친구와 직선거리 합이 1:
            - cnt += 1
    - happiness 누적
- print(happiness)
'''

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