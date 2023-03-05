'''
빨간 + 초록
빨강의 경계선(행) 까지 간다음에.. 끝까지..
한칸씩 내려가기 부딪히면 전으로 돌아가는거
특별한 행에 위치한지 확인
    지우기, 만들기
4칸 다 찾는지 확인
    지우기 만들기
빨간 + 파란
빨강 경계선 (열) 까지 간다음에 .. 끝까지
한칸씩 오른쪽으로 부딪히면 전으로 돌아가는거
특별한 열에 위치했는지 확인
    지우기, 만들기
4칸 다 찾는지 확인
    지우기 만들기
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
        if sum(area[i]) == 0:
            continue
        area = [[0] * 4] + area[:-1] # 블록 있으면 한칸 밀어내기
    return area

blue, green = [[0]*4 for _ in range(6)], [[0]*4 for _ in range(6)] # 연한 영역 포함해 구성
ans = 0 # 획득 점수

# main
for _ in range(int(input())):
    push(*map(int, input().split())) # t, x, y 입력 -> 쌓기
    blue = pop(blue)
    green = pop(green)

print(ans)
print(sum(map(sum, blue)) + sum(map(sum, green)))
