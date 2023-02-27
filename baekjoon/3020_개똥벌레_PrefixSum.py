'''
imos 법
입장시 +1, 최장시 -1.
각 명령에 대해 시작점과 끝점만 설정해 준 뒤, 마지막에 한 번의 반복을 통해 값을 계산

장애물 최솟값을 구하는 것이므로, 중앙이 가장 최소값
'''

from sys import stdin
I = stdin.readline

N, H = map(int, I().split()) # 길이, 높이

arr = [0]*(H+1) # 높이 정보들. 높이는 7이지만 기준점 0 포함해야함.
for i in range(N):
    if i % 2: # 종유석
        arr[H] -= 1 # 종료점
        arr[H-int(I())] += 1 # 시작점
    else: # 석순
        arr[0] += 1 # 시작점
        arr[int(I())] -= 1 # 종료점

# arr[0] == 석순 개수
# arr[H] == 종유석 개수

prefix = [0] * H # 높이에 따라 걸리는 개수 계산
for i in range(H):
    prefix[i] = arr[i] + prefix[i-1] # arr[H+1] + prefix[H+1]은 어차피 0이 될 것이므로 제외. prefix == 누적 arr.

count = 0
norm = prefix[0] # 시작점(석순의 수 == 종유석의 수)을 기준값으로 편의상 설정.

for value in prefix:
    if value == norm:
        count += 1
    if value < norm: # 기준값 갱신
        norm = value
        count = 1 # 초기화

print(norm, count)