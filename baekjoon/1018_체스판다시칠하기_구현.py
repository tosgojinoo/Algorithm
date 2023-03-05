'''
[설명]
M×N 크기의 보드 -> 보드를 잘라서 8×8 크기의 체스판
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색
체스판은 검은색과 흰색이 번갈아서  -> 변을 공유하는 두 개의 사각형은 다른 색
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우
체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다

[문제] 지민이가 다시 칠해야 하는 정사각형의 최소 개수
'''
'''
- 브루트 포스: 시작점 조건이 없어, 특정할 수 없음
- 브루트 포스 범위: 
    - 8×8 크기의 체스판
    - 0 ~ N/M-8+1 까지 설정
- 최소 색칠 개수:
    - W 시작, B 시작 각각 cnt
    - 매 시작점 선정시 마다 초기화
- 색 감지 패턴:
    - (ny + nx) % 2
    - 기준점부터 짝수 거리 지점은 색 동일. 홀수 거리는 반대.
'''
'''
[구조]
- arr로 체스판 현황 받음
- 브루트 포스로 기준점 선정 (y/x를 0 ~ N/M-7까지 탐색)
    - B/W로 각각 시작하는 cnt 변수 설정
    - 기준점부터 y/x+7까지 범위내 탐색
        - 좌표 패턴 조건
            - B/W 상태에 따라 cnt 추가
    - result에 cnt 저장
- min(resilt) 출력  
'''
N, M = map(int, input().split())
result = []
arr = [list(input()) for _ in range(N)]

for y in range(N - 8 + 1):
    for x in range(M - 8 + 1):
        draw1, draw2 = 0, 0 # 'B' / 'W' 각각으로 시작했을 때 cnt

        for ny in range(y, y + 7 + 1):
            for nx in range(x, x + 7 + 1):
                if not (ny + nx) % 2: # 좌표의 합으로 패턴 선정
                    if arr[ny][nx] != 'B':
                        draw1 += 1
                    if arr[ny][nx] != 'W':
                        draw2 += 1
                else:
                    if arr[ny][nx] != 'W':
                        draw1 += 1
                    if arr[ny][nx] != 'B':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))