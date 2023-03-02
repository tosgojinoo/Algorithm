import sys
input = sys.stdin.readline

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]

tot = sum(map(sum, zip(*arr))) # 전체 인구 합
for i in range(n):
    for j in range(1, n):
        arr[i][j] += arr[i][j-1] # 행 누적합 방식으로 변경

res = float("inf")
# d1, d2를 조건에 따라 변경하면서, x,y 탐색 결과의 최대값 저장
for d1 in range(1, n-2): # 문제 제공. 1 ≤ x < x+d1+d2 ≤ N -> N-1-1 >= d1. idx 1부터 시작 감안. 길이이므로 1 이상.
    for d2 in range(1, n-1-d1): # 문제 제공. 1 ≤ x < x+d1+d2 ≤ N -> N-1-d1 >= d2. idx 1부터 시작 감안. 길이이므로 1 이상.
        for x in range(n-d1-d2): # 문제 제공. 1 ≤ x < x+d1+d2 ≤ N -> N-d1-d2 >= x. idx 1부터 시작 감안.
            for y in range(d1, n-d2): # 문제 제공. 1 ≤ y-d1 < y < y+d2 ≤ N -> y = d1+1 ~ N-d2. idx 1부터 시작 감안. 
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
# d1, d2를 조건에 따라 변경하면서, x,y 탐색 결과의 최대값 저장
for d1 in range(1, n-2): # 문제 제공. 1 ≤ x < x+d1+d2 ≤ N -> N-1-1 >= d1. idx 1부터 시작 감안. 길이이므로 1 이상.
    for d2 in range(1, n-1-d1): # 문제 제공. 1 ≤ x < x+d1+d2 ≤ N -> N-1-d1 >= d2. idx 1부터 시작 감안. 길이이므로 1 이상.
        for x in range(n-d1-d2): # 문제 제공. 1 ≤ x < x+d1+d2 ≤ N -> N-d1-d2 >= x. idx 1부터 시작 감안.
            for y in range(d1, n-d2): # 문제 제공. 1 ≤ y-d1 < y < y+d2 ≤ N -> y = d1+1 ~ N-d2. idx 1부터 시작 감안.
                print(d1, d2, x, y)
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