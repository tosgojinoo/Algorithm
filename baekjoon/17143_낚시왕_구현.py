'''
방향 전환 수식 필요
new_arr 사용 판단
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
for j in range(C): # 열 방향으로 1칸씩 이동/
    # 낚시
    for i in range(R): # 낚시왕 최근거리부터 확인
        if arr[i][j]: 
            answer += arr[i][j][2] # 크기
            arr[i][j] = None
            break # 상어 잡으면 종료.

    # 상어 이동
    new_arr = [[None] * C for _ in range(R)] # 
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
