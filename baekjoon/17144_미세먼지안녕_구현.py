'''
[설명]
R×C
(r, c)는 r행 c열
- 공기청정기
    - 1번 열에 설치
    - 크기 두 행 차지
    - 공기청정기가 설치되어 있지 않은 칸에는 미세먼지
    - 공기청정기가 설치된 곳은 A(r,c) == -1
    - -1은 2번 위아래로 붙어 있음
    - 가장 윗 행, 아랫 행과 두 칸이상 이격
- 미세먼지
    - (r, c)에 있는 미세먼지의 양은 A(r,c)
- 1초 동안
    - 미세먼지 확산.
        - 모든 칸에서 동시에.
        - (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산 -> dxy
        - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 확산 x -> 제한 조건: 범위 밖, 공기청정기
        - 확산되는 양은 Ar,c/5이고 소수점은 버린다. -> A(r,c) //5
        - (r, c)에 남은 미세먼지의 양은 A(r,c) - (A(r,c)/5)×(확산된 방향의 개수)
    - 공기청정기 작동
        - 위쪽 공기청정기의 바람은 반시계방향으로 순환 -> 공청기 행은 오른쪽, 끝 열에서 위로, 첫 행에서 왼쪽, 공청기 열에서 아래로.
        - 아래쪽 공기청정기의 바람은 시계방향으로 순환 -> 공청기 행은 오른쪽, 끝 열에서 아래로, 마지막 행에서 왼쪽, 공청기 열에서 위로.
        - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
        - 공기청정기에서 부는 바람은 미세먼지가 없는 바람
        - 공기청정기로 들어간 미세먼지는 모두 정화

[문제]
T초가 지난 후 방에 남아있는 미세먼지의 양
'''
'''
[알고리즘]
- arr
    - new_arr 사용
    - 이전 칸에서 spread 된 것을 이후 칸에서 재분배하면 안됨
    - 새롭게 arr 구성 후 업데이트가 편리함
- 먼지 분배
    - 최초값 저장
    - 단위 분배량 계산 후 실질적으로 분배된 만큼을 최초값에서 차감
    - 차감된 최초값을 원래 위치에 저장
- 이동
    - 우/하 방향: 역순으로 업데이트 해야함
'''
'''
[구조]
- arr 저장
- for T 횟수만큼
    - spread()
    - purify()
- 출력: 2(공청기 -1*2) + sum(map(sum, zip(*arr)))

- spread()
    - new_arr 빈 arr 구성
    - for 전체 탐색
        - if 먼지
            - 최초값 저장
            - 단위 분배량 계산 (5로 나눈 몫)
            - for 4방향
                - if 범위 내 & 공청기 아님
                    - 분배량을 각 칸에 분배
                    - 최초값에서 분배된 값 차감
            - 최초값의 잔량을 해당칸에 저장 
        - elif 공청기
            - 공청기 위치 기록
    - return new_arr

- purify():
    - for 공청기 위치 중 윗칸 좌표 확인
        - if 공청기: break

    - for 공청기 열. 바로 윗 부분. 아래부터 위로 역순: 이동  
    - for 첫 행. 왼쪽부터: 이동
    - for 맨 우측 열. 공청기 윗쪽 범위만. 위로: 이동
    - for 공청기 윗칸 행. 오른쪽에서 왼쪽. 역순: 이동
    
    - 공청기 중 위에서 나온 곳 == 0
    
    - 공청기 두칸 중 아래칸 좌표 확인
    
    - for 공청기 열. 바로 아랫 부분. 공정기 아래쪽 범위만: 이동
    - for 마지막 행. 왼쪽부터: 이동
    - for 맨 우측 열. 공청기 아래쪽 범위만. 아래로. 역순: 이동
    - for 공청기 아래칸 행. 오른쪽에서 왼쪽. 역순: 이동
    
    - 공청기 중 아래칸에서 나온 곳 == 0
    
    - return arr

'''


import sys
input = sys.stdin.readline


def spread():
    new_arr = [[0]*C for _ in range(R)] # spread 된 것을 재분배하면 안되기 때문에, 새롭게 arr 구성 후 업데이트가 편리함.
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0: # 먼지
                prev = arr[i][j] # 최초값 저장
                spr = prev//5 # 단위 분배량
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0<=ni<=R-1 and 0<=nj<=C-1 and arr[ni][nj] != -1:
                        new_arr[ni][nj] += spr
                        prev -= spr
                new_arr[i][j] += prev
            elif arr[i][j] == -1: # 공청기
                new_arr[i][j] = -1 # 공청기 위치
    return new_arr


def purify():
    # 공청기 위치 확인. 윗 좌표.
    for purifier in range(R):
        if arr[purifier][0] == -1:
            break

    for i in range(purifier-1, 0, -1): # 공청기 열. 바로 윗 부분. 아래로 1칸씩
        arr[i][0] = arr[i-1][0]
    for j in range(C-1): # 0번 행. 왼쪽으로 1칸씩
        arr[0][j] = arr[0][j+1]
    for i in range(purifier): # 마지막 행. 공청기 윗쪽. 위로 1칸씩
        arr[i][C-1] = arr[i+1][C-1]
    for j in range(C-1, 1, -1): # 공청기 윗 행. 오른쪽 1칸씩
        arr[purifier][j] = arr[purifier][j-1]
    arr[purifier][1] = 0 # 공청기 중 위에서 나온 곳
    purifier += 1 # 공청기 두칸 중 아래칸
    for i in range(purifier+1, R-1): # 공청기 열. 바로 아랫 부분.
        arr[i][0] = arr[i+1][0]
    for j in range(C-1): # 맨 아래 행
        arr[R-1][j] = arr[R-1][j+1]
    for i in range(R-1, purifier, -1): # 맨 오른쪽 열
        arr[i][C-1] = arr[i-1][C-1]
    for j in range(C-1, 1, -1): # 공청기 아래 행.
        arr[purifier][j] = arr[purifier][j-1]
    arr[purifier][1] = 0 # 공청기 중 아래칸에서 나온 곳
    return arr


R, C, T = map(int, input().split()) # 격자 R/C. T초후.
arr = [list(map(int, input().split())) for _ in range(R)]
for _ in range(T):
    arr = spread()
    arr = purify()
ans = 2 # 공청기가 -1씩 2개 있음
ans += sum(map(sum, zip(*arr)))
print(ans)