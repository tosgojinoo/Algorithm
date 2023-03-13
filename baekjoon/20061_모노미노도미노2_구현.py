'''
[설명]
빨간색 보드, 파란색 보드, 초록색 보드가 그림과 같이 붙어있는 형태
(x, y)에서 x는 행, y는 열
블록은 타일 하나 또는 두 개가 가로 또는 세로로 붙어있는 형태
아래와 같이 세 종류가 있으며, 크기가 1×1, 1×2, 2×1
블록을 놓을 위치를 빨간색 보드에서 선택하면, 그 위치부터 초록색 보드로 블록이 이동하고, 파란색 보드로 블록이 이동
블록의 이동은 다른 블록을 만나거나 보드의 경계를 만나기 전까지 계속해서 이동
블록은 보드에 놓인 이후에 다른 블록과 합쳐지지 않음

- 타일 == 블록들
    - 어떤 행이 타일로 가득 차 있다면, 그 행의 타일은 모두 사라짐
    - 초록색: 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동
    - 파란색: 사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동
    - 행/열이 사라지면 1점을 획득
    - 점수는 사라진 행 또는 열의 수
- 연한색 구간
    - 초록색 보드의 0, 1번 행
    - 파란색 보드의 0, 1번 열
    - 초록색
        - 초록색 보드의 0, 1번 행에 블록이 있으면,
        - 블록이 있는 행의 수만큼 아래 행에 있는 타일이 사라지고,
        - 초록색 보드의 모든 블록이 사라진 행의 수만큼 아래로 이동,
    - 파란색
        - 파란색 보드의 0, 1번 열에 블록이 있으면,
        - 블록이 있는 열의 수만큼 오른쪽 열에 있는 타일이 사라지고,
        - 파란색 보드의 모든 블록이 사라진 열의 수만큼 이동
- 순서
    - 행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생
    - 1. 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행
    - 2. 연한 칸에 블록이 있는 경우를 처리

- 블록 종류
    - t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
    - t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
    - t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우

[문제]
- 블록을 모두 놓았을 때 얻은 점수
- 파란색 보드와 초록색 보드에서 타일이 들어있는 칸의 개수
'''
'''
[알고리즘]
- 한칸씩 이동하다 부딪히면 처리하는 방식 x -> 계산량 증가
- 기준점 
    - col 좌표 변동 없음
    - row 좌표만 계산. top() 사용.
- blue, green
    - 연한색 구간 포함 범위
    - 6 x 4로 동일 구성
    - 동일 처리 함수 적용 가능
    - 방향만 90도 회전
- push()
    - blue, green 한번에 쌓기
    - 방향 고려한 x, y 좌표 전환 후 쌓기
    - blue: 수평방향, green: 수직방향
    - 블록을 놓고 내리는 방식 x
    - push() 진입하자마자 바로 쌓음
    - 쌓을 때, 열값은 변하지 않고, 기존 타일 위치에 따라 행 값만 변경(green 방향 기준)
    - top()을 통해 최대 높이 계산 (이미 놓여있는 블록의 윗 행 값 리턴)
    - t == 2,3
        - 날개 방향까지 고려한 최상단(min(row)) 계산 반영 
        - 최상단 계산은 항상 min(row 기준점, top(green/blue, col 기준점 + 1)
        - green, blue 모두 동일
        - 날개를 감안한 각 방향 최상단 row를 먼저 계산 후 기준점을 기록함
- top()
    - 열 탐색 후 최상 위치의 행값 리턴
    - 색 선택 -> 연한색 부분 제외 영역 -> col 위치 입력 -> 그중 가장 높은 row의 바로 윗 row 리턴

- pop()
    - 영역별 회전 없이 계산
'''
'''
[구조]
- blue, green = 6 x 4 array

- for 블록을 놓은 횟수 N: 
    - push((블록을 놓은 정보 t, x, y))
    - pop(blue) 
    - pop(green)

- print(ans) # 획득 점수
- print(sum(map(sum, blue)) + sum(map(sum, green))) # 타일 개수

- push(t, x, y): # 기준점 x,y
    # 추가된 블록의 각 방향 열 기준값
    - blue_c, green_c = x, y 
    # 추가된 블록의 각 방향 열 기준값 내 가장 높은 행의 이전 행 값 
    - blue_r, green_r = top(blue, blue_c), top(green, green_c) 
    - if 가로 두칸:
        - green_r = min(green_c 기준 상단, green_c+1 기준 상단) # 최상단(더 작은 row)
        - green 영역, 날개 추가
        - blue 영역, 기준점 위로 추가
    - elif 세로 두칸:
        - blue_r = min(blue_r 기준 상단, top(blue, blue_c+1))
        - blue 영역, 날개 추가
        - green 영역, 기준점 위로 추가
    - 기준점에 추가

- top(area, col): 
    - for 연한 블록 제외한 영역:
        - if 타일 있으면:
            - return 해당 row의 윗 row
    - return 마지막 행값(5)

- pop(area):
    # 연한색 영역 제외한 영역 우선.
    - for green/blue 영역: 
        - if 행 중에 빈 곳 있음: 무시
        - 삭제 후 맨 앞에 한줄 채우기
        - 점수 추가 ans ++ 
    # 연한색 영역
    - for 연한색 영역:
        - if 행 전체 비어 있음: 무시
        - 블록 있으면 한칸 밀어내기
    - return area
'''

import sys
input = sys.stdin.readline

def top(area, col): # 열 탐색 후 최상 위치의 행값 리턴
    for row in range(2, 6): # 연한 블록 제외한 순수 영역
        if area[row][col]: #
            return row - 1
    return 5 # 마지막 행값


def push(t, x, y): # 쌓을 때 방향 고려한 x, y 좌표 전환 후 적용.
    '''
    t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
    t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
    t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
    '''

    blue_c, green_c = x, y # blue: 수평방향, green: 수직방향
    blue_r, green_r = top(blue, blue_c), top(green, green_c)
    if t == 2:
        green_r = min(green_r, top(green, green_c+1)) # 한번더 top 확인 후 더 낮은(상단) 값 저장
        green[green_r][green_c+1], blue[blue_r-1][blue_c] = 1, 1 # 날개부분. blue/green 최상단에 1개씩 놓임
    elif t == 3:
        blue_r = min(blue_r, top(blue, blue_c+1))
        blue[blue_r][blue_c+1], green[green_r-1][green_c] = 1, 1 # 날개부분. blue/green 최상단에 1개씩 놓임
    blue[blue_r][blue_c], green[green_r][green_c] = 1, 1 # 중심점. blue/green 최상단에 1개씩 놓임


def pop(area): # 한줄 전체가 1일 경우 삭제. 입력 area 방향 회전 필요 없음.
    global ans
    for i in range(2, 6): # 연한 영역 제외한 순수 영역만. 삭제할 줄 먼저 계산.
        if sum(area[i]) != 4: # 빈 곳 있음
            continue
        area = [[0] * 4] + area[:i] + area[i+1:] # 삭제 후 맨 앞에 한줄 채우기
        ans += 1 # 점수 추가

    for i in range(0, 2): # 연한 영역.
        if not sum(area[i]):
            continue
        area = [[0] * 4] + area[:-1] # 블록 있으면 한칸 밀어내기
    return area


blue, green = [[0]*4 for _ in range(6)], [[0]*4 for _ in range(6)] # 연한 영역 포함해 구성
ans = 0 # 획득 점수

# main
for _ in range(int(input())): # 블록을 놓은 횟수 N
    push(*map(int, input().split())) # 블록을 놓은 정보 t, x, y 입력 -> 쌓기
    blue = pop(blue)
    green = pop(green)

print(ans)
print(sum(map(sum, blue)) + sum(map(sum, green)))
