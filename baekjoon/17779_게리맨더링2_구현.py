'''
[설명]
N×N
r행 c열에 있는 구역은 (r, c)
구역을 다섯 개의 선거구로 나눔
각 구역은 다섯 선거구 중 하나에 포함
선거구는 구역을 적어도 하나 포함
선거구에 포함되어 있는 구역은 모두 연결
모두 같은 선거구에 포함된 구역
- 선거구를 나누는 방법
    - 기준점 (x, y)와 경계의 길이 d1, d2
        - (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
    - 경계선
        - (x, y), (x+1, y-1), ..., (x+d1, y-d1)
        - (x, y), (x+1, y+1), ..., (x+d2, y+d2)
        - (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
        - (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
    - 경계선과 경계선의 안에 포함되어 있는 곳은 5번 선거구
    - 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호 기준
        - 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
        - 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
        - 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
        - 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
구역 (r, c)의 인구는 A[r][c]
선거구의 인구는 선거구에 포함된 구역의 인구를 모두 합한 값
r행 c열의 정수는 A[r][c]를 의미

[문제]
인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값
'''
'''
[알고리즘]
- arr 전환
    - 영역과 영역을 나누는 경계가 있고, 
    - 경계를 기준으로 영역내 숫자 합을 활용하는 경우
    - 우측으로 행 별 누적합 arr을 재구성
    - 경계값 or (우측값-경계값) 활용하면 계산량 감소 
- 변수 제한
    - d1, d2, x, y 공통적으로 문제 내 관계식 활용
    - idx -1 shift가 필요하기에, range(0 ~ N)이 기본값. (N은 자연스럽게 제외) 
    - d1, d2
        - 길이
        - 항상 1보다 큰 범위 적용
    - x, y
        - 0이상 범위 적용
    - 계산 범위의 지정
        - x만 제한해도 됨.
        - 모든 값이 수식으로 엮여있음 (닫힌 도형이기 때문)
'''
'''
[구조]
- arr 저장
    - 우측 행 별 누적합 방식으로 arr 변경
    
- 경계 길이 d1, d2를 조건에 따라 변경하면서, x,y 탐색 결과의 최대값 저장
(- idx -1 shift 적용)
# 1 ≤ x < x+d1+d2 ≤ N -> d1 <= N-1(d2)-1(x). 길이 이므로 1 이상.
- for d1 in range(1, n-2): 
    # 1 ≤ x < x+d1+d2 ≤ N -> d2 <= N-d1-1(x). 길이 이므로 1 이상.
    - for d2 in range(1, n-1-d1): 
        # 1 ≤ x < x+d1+d2 ≤ N -> x <= N-d1-d2. x 는 0 가능 
        - for x in range(n-d1-d2): 
            # 1 ≤ y-d1 < y < y+d2 ≤ N -> y = d1+1 ~ N-d2.
            - for y in range(d1, n-d2): 
                - group1, group2, group3, group4 = 0 초기화
                
                # 시작 꼭지점(x,y) 바로 위까지 
                - for r in range((x-1)+1): 
                    # y까지 누적 -> group1 저장
                    - group1 += arr[r][y] 
                    # 행누적 - y까지 누적 -> group2 저장
                    - group2 += arr[r][-1]-arr[r][y] 
                
                # 1. 시작 꼭지점 ~ 마름모 중간. 왼쪽.
                - for r1 in range(x, (x+d1-1)+1): 
                    # 대각선 왼쪽으로 감소하며 누적값 -> group1
                    # '증분' 에 (0 <= A <= d1-1) 을 만족하는 (A == -(r1-x) ~ -d1 <- x-d1 = r1) 추가
                    - group1 += arr[r1][(y-1)-(r1-x)] 
                
                # 2. 시작 꼭지점 ~ 마름모 중간. 오른쪽
                - for r2 in range(x, (x+d2)+1): 
                    # 전체 누적값 - 경계 누적값 -> group2
                    # '증분' 에 (0 <= B <= d2) 을 만족하는 (B == r2-x <- x+d2 = r2) 추가
                    - group2 += arr[r2][-1]-arr[r2][y+(r2-x)] 
                
                # 3. 마름모 중간 ~ 아래. 왼쪽. '1'의 끝+1 == 시작.
                - for r3 in range(x+d1, (x+d1+d2)+1):
                    # 대각선 오른쪽으로 감소하며 누적값 -> group3
                    # y-d1 조건 주의 (y <= d1 불가!)   
                    # '증분' 에 (0 <= C <= d2) 을 만족하는 (C == r3-x+d1 ~ d2 <- x-d1+d2 = r3) 추가
                    group3 += arr[r3][((y-d1)-1)+(r3-x-d1)] if y - d1 else 0
                
                # 4. 마름모 중간 ~ 아래. 오른쪽. '2'의 끝+1 == 시작.
                - for r4 in range(x+d2+1, (x+d1+d2)+1): 
                    # 전체 누적값 - 경계 누적값 -> group4
                    # '증분' 에 (1 <= D <= d1) 을 만족하는 (D == -(r4-x-d2) ~ -d1 <- x+d1+d2 = r4) 추가
                    - group4 += arr[r4][-1]-arr[r4][(y+d2)-(r4-x-d2] 
                
                # 아래 꼭지점 이후 아래로
                - for r in range((x+d1+d2)+1, n): 
                    # 누적
                    - group3 += arr[r][(y-d1+d2)-1] 
                    # 누적차
                    - group4 += arr[r][-1]-arr[r][(y-d1+d2)-1] 
                
                - a, _, _, _, b = sorted([group1, group2, group3, group4, tot-group1-group2-group3-group4])
                - res = res if b-a>res else b-a # 제일 큰 그룹 - 작은 그룹
'''


import sys
input = sys.stdin.readline

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]

tot = sum(map(sum, zip(*arr))) # 전체 인구 합
for i in range(n):
    for j in range(1, n):
        arr[i][j] += arr[i][j-1] # 행 누적합 방식으로 변경

res = float("inf")

for d1 in range(1, n-2):
    for d2 in range(1, n-1-d1):
        for x in range(n-d1-d2):
            for y in range(d1, n-d2):
                group1, group2, group3, group4 = 0, 0, 0, 0
                for i in range(x): # 시작 꼭지점(x,y) 바로 위까지.
                    group1 += arr[i][y] # y까지 누적 -> group1
                    group2 += arr[i][-1]-arr[i][y] # 행누적 - y까지 누적 -> group2
                for i in range(x, x+d1): # 시작 꼭지점 ~ 마름모 중간.
                    group1 += arr[i][y-1-i+x] # 대각선 왼쪽으로 감소하며 누적값 -> group1
                for i in range(x, x+d2+1): # 시작 꼭지점 ~ 마름모 중간.
                    group2 += arr[i][-1]-arr[i][y+i-x] # 전체 누적값 - 경계 누적값 -> group2
                for i in range(x+d1, x+d1+d2+1): # 마름모 중간 ~ 아래.
                    group3 += arr[i][y-d1-1+i-x-d1] if y - d1 else 0 # 대각선 오른쪽으로 감소하며 누적값 -> group3. y-d1 조건 주의.
                for i in range(x+d2+1, x+d1+d2+1): # 마름모 중간 ~ 아래.
                    group4 += arr[i][-1]-arr[i][y+d2-i+x+d2] # 전체 누적값 - 경계 누적값 -> group4.
                for i in range(x+d1+d2+1, n): # 아래 꼭지점 이후 아래부터.
                    group3 += arr[i][y-d1+d2-1] # 누적
                    group4 += arr[i][-1]-arr[i][y-d1+d2-1] # 누적차
                a, _, _, _, b = sorted([group1, group2, group3, group4, tot-group1-group2-group3-group4])
                res = res if b-a>res else b-a # 제일 큰 그룹 - 작은 그룹

print(res)


''' 확인용
                group1, group2, group3, group4 = [], [], [], []
                for i in range(x): # 시작 꼭지점(x,y) 바로 위까지.
                    group1.append(f'{arr[i][y]}') # y까지 누적 -> group1
                    group2.append(f'{arr[i][-1]}-{arr[i][y]}') # 행누적 - y까지 누적 -> group2
                for i in range(x, x+d1): # 시작 꼭지점 ~ 마름모 중간.
                    group1.append(f'{arr[i][y-1-i+x]}') # 대각선 왼쪽으로 감소하며 누적값 -> group1
                for i in range(x, x+d2+1): # 시작 꼭지점 ~ 마름모 중간.
                    group2.append(f'{arr[i][-1]}-{arr[i][y+i-x]}') # 대각선 오른쪽으로 감소하며 누적값 -> group2
                for i in range(x+d1, x+d1+d2+1): # 마름모 중간 ~ 아래.
                    print(arr[i][y-d1-1+i-x-d1], y, d1, x, d2)
                    group3.append(f'{arr[i][y-d1-1+i-x-d1] if y-d1 or i>1 else 0}') # 대각선 오른쪽으로 감소하며 누적값 -> group3
                for i in range(x+d2+1, x+d1+d2+1): # 4번 선거구: x+d2 < r ≤ N. 경계선 조건 x+d1+d2 ≤ N
                    group4.append(f'{arr[i][-1]}-{arr[i][y+d2-i+x+d2]}')
                for i in range(x+d1+d2+1, n): # 1 ≤ x < x+d1+d2 ≤ N. 뒷부분
                    group3.append(f'{arr[i][y-d1+d2-1]}')
                    group4.append(f'{arr[i][-1]}-{arr[i][y-d1+d2-1]}')
                print(group1, group2, group3, group4)

print(res)
'''