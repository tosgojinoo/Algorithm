'''
[설명]
R×C
(r, c), r은 행, c는 열
(R, C)는 아래 그림에서 가장 오른쪽 아래에 있는 칸
- 낚시왕
    - 처음에 1번 열의 한 칸 왼쪽
    - 가장 오른쪽 열의 오른쪽 칸에 이동하면 종료 -> for 열방향 이동
    - 다음은 1초 동안 일어나는 일 -> 계산 순서 반영
        1. 낚시왕이 오른쪽으로 한 칸 이동
        2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡음
            상어를 잡으면 격자판에서 잡은 상어가 사라진다.
        3. 상어가 이동
- 상어
    - 칸에는 상어가 최대 한 마리
    - 상어는 크기와 속도
    - 상어는 입력으로 주어진 속도로 이동
    - 속도의 단위는 칸/초
    - 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동
        -> 경계 밖, 방향 반대 속도 유지, 이동
        -> dxy 조건: 상하, 좌우를 붙여 구성. 계산 용이하도록.
        -> 방향 전환 조건: 행/열 크기로 나눈 몫이 2의 배수 여부에 따라 상하/좌우 반대 전환
    - 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 경우,
        크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹음 -> 크기가 더 큰 상어로 지속 update

- dxy
    - 1 위, 2 아래, 3 오른쪽, 4 왼쪽
    - 벽일 경우, 1 <-> 2, 3 <-> 4

[문제]
낚시왕이 잡은 상어 크기의 합을 출력
'''
'''
[알고리즘]
- dxy
    - 상하, 좌우 붙여서 배열. 반대방향 전환 계산 편의상.
    - idx 1 부터 시작
        - idx 0에 (0,0) 삽입
        - or, idx -1 shift
- arr
    - 상어 이동 전후 정보 변경시
        - 단일 arr 사용
            - 이후 값 기록, 이전값 삭제 -> 2번 * 상어수 만큼 작업
        - new_arr 사용
            - 이후 값만 기록, arr 바뀌치기 -> 1번 * 상어수 + 1회 작업 => 계산량 감소, 편함 => 채택
    - idx -1 shift 관련
        - 0을 padding으로 포함한 구성하게 될 경우, 방향 전환 계산시 까다로워짐. 전체적으로 -1 shift로 idx 구성.
- 탐색 순서
    - 열방향 이동
        - 낚시
            - 행방향 최근 거리 상어 잡으면 break
        - 상어 이동
            - 탐색, 열 우선 > 행
                - 상어 정보 확인
                - (현위치 + 속도*방향)을 열 or 행으로 나눈 몫이 2배수냐 아니냐에 따라 방향 전환 판단 
                - 상하 / 좌우 이동 구분
                - 역방향
                    - 좌우: ((d - 2) % 2) + 3
                    - 상하: (d % 2) + 1
'''
'''
[구조]
- arr[r][c] 에 (상어 속력, 이동 방향, 크기) 저장
- for 열방향, 1칸씩 이동
    - 낚시
        - for 행방향, 낚시왕 최근거리 확인
            - if 상어: 
                - 크기 누적
                - 해당 arr은 None 처리
                - 상어 잡았으니 break
    - 상어 이동
        - new_arr 준비, 빈 arr
        - for 행방향, 탐색
            - for 열방향, 탐색
                - if 상어 없으면 무시
                - 상어 정보 확인
                - if 좌우. 수평 이동.
                    - 몫, 나머지 = divmod((현위치 + 속도*방향), 열크기)
                    - if 몫 == 짝수
                        - 방향 유지, 나머지 만큼만 이동
                    - else 몫 == 홀수.
                        - 역방향, 열 기준 나머지의 역수만큼 이동
                - else 상하. 수직 이동.
                    - 몫, 나머지 = divmod((현위치 + 속도*방향), 행크기)
                    - if 몫 == 짝수. 
                        - 방향 유지, 나머지 만큼만 이동
                    - else 몫 == 홀수
                        - 역방향, 행 기준 나머지의 역수만큼 이동
    
                - if 아직 입력 전 or 이미 입력된 상어보다 클 경우.
                    new_arr[nr][nc] = (s, d, z)

    - new_arr 로 arr update

'''

import sys

input = sys.stdin.readline

direction = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)] # 상, 하, 우, 좌. idx 1부터 시작하여, (0,0) 추가. 

R, C, M = map(int, input().split()) # 상어 정보 M

arr = [[None] * C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split()) # 상어의 위치 (r, c), 속력 s, 이동 방향 d, 크기 z
    arr[r - 1][c - 1] = (s, d, z) # idx가 1부터 시작. shifting.

answer = 0
for j in range(C): # 열 방향으로 1칸씩 이동
    # 낚시
    for i in range(R): # 낚시왕 최근거리부터 확인
        if arr[i][j]: 
            answer += arr[i][j][2] # 크기
            arr[i][j] = None
            break # 상어 잡으면 종료.

    # 상어 이동
    new_arr = [[None] * C for _ in range(R)]
    for r in range(R): # 차례대로. 행 우선 -> 열 순서
        for c in range(C):
            if not arr[r][c]: # 상어 없으면 무시.
                continue
            s, d, z = arr[r][c] # 상어 정보 확인.

            if d > 2: # 우, 좌. 수평 이동
                nr = r
                nc = c + s * direction[d][1]
                qc, rc = divmod(nc, C - 1)
                if qc % 2 == 0: # 몫 == 짝수. 나머지 만큼만 이동.
                    nc = rc
                else: # 몫 == 홀수.
                    d = ((d - 2) % 2) + 3 # 3 -> 4, 4 -> 3
                    nc = (C - 1) - rc # C-1 기준 역수
            else: # 상, 하. 수직 이동.
                nc = c
                nr = r + s * direction[d][0]
                qr, rr = divmod(nr, R - 1)
                if qr % 2 == 0: # 방향 유지
                    nr = rr
                else: # 역방향
                    d = (d % 2) + 1 # 1 -> 2, 2 -> 1
                    nr = (R - 1) - rr # R-1 기준 역수

            if not new_arr[nr][nc] or new_arr[nr][nc][2] < z: # 아직 입력 전 or 이미 입력된 상어보다 클 경우.
                new_arr[nr][nc] = (s, d, z)

    arr = new_arr # arr update

print(answer)
