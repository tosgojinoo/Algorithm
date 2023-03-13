'''
[설명]
크기가 N×N
도시의 각 칸은 빈 칸, 치킨집, 집 중 하나. 0은 빈 칸, 1은 집, 2는 치킨집.
r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미
r과 c는 1부터 시작 -> idx -1 shift

치킨 거리는 집과 가장 가까운 치킨집 사이의 거리 -> 치킨집과의 거리들 중 최소값
치킨 거리는 집을 기준으로 정해짐
각각의 집은 치킨 거리를 가지고 있다.
도시의 치킨 거리는 모든 집의 치킨 거리의 합
임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|

1<= 집의 개수 <=2N
M<= 치킨집의 개수 <=13

[문제]
폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, -> 개수 제한 없음 -> combinations()
도시의 치킨 거리의 최솟값 -> 누적 거리 최소
'''
'''
[알고리즘]
- 누적 거리 최소 계산 & 치킨집 개수 제한 없음
    -> 치킨집 조합 -> 집과의 거리가 최소가 되는 경우 도출
'''
'''
[구조]
- arr 저장
- house, chicken 리스트
- 집, 치킨집 위치 우선 저장
- for 치킨집 combinations
    - for house
        - for 치킨집 case
            - min_dist = min(min_dist, 치킨집거리)
        - min_dist 누적
    result = min(min_dist)
'''


from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)
arr = [list(map(int, input().split())) for _ in range(n)]
house = []
chick = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: # 집
            house.append((i, j))
        elif arr[i][j] == 2: # 치킨집
            chick.append((i, j))

res = 1e9
for case in combinations(chick, m):
    tmp = 0
    for hx, hy in house:
        mini = 1e9
        for cx, cy in case:
            mini = min(mini, abs(hx - cx) + abs(hy - cy))
        tmp += mini
    res = min(res, tmp) # 누적 직선거리 최소값 출력
print(res)