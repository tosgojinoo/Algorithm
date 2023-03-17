'''
[설명]
N개의 구역
구역은 1번부터 N번까지
구역을 두 개의 선거구로 나눔
각 구역은 두 선거구 중 하나에 포함
선거구는 구역을 적어도 하나 포함
한 선거구에 포함되어 있는 구역은 모두 연결
구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결
중간에 통하는 인접한 구역은 0개 이상
모두 같은 선거구에 포함된 구역

[문제]
두 선거구로 나누었을 때, 두 선거구의 인구 차이의 최솟값
두 선거구로 나눌 수 없는 경우에는 -1
'''
'''
[알고리즘]
- memory
    - arr
        - arr[정보번호][인접 구역 idx들] = 1
        - arr[[0,0,1,1,0,0],...]
    - weights
        - 구역의 인구수 array
        
- combination
    - 두 그룹으로 나눌 경우, (1~절반) 까지 대상만으로 case만 확인
    - A & B == B & A
    
- array_total에서 array_sub 원소들만 제거하기 
    - set(array_total).difference(array_sub)
    
- BFS
    - BFS 가능 == 정상 그룹 형성 가능
    - 방문 총 횟수와 그룹 숫자가 동일해야 성립
        - visited.count(True) == len(group) 
    - 가지치기 조건
        - if 이어지지 않음: 무시
        - if 그룹에 불포함 구역: 무시
        - if 미방문: queue 추가
'''
'''
[구조]
- weights = list(map(int, input().split())) # 구역의 인구수
- arr[정보번호][인접 구역 idx들] = 1

- for range(1, N // 2 + 1): 절반의 대상만을 case로  
    - A_cases = tuple(comb(list(range(N)), i))
    - for A_cases:
        - B = list(set(nums).difference(A)) # nums 와 A 간 다른 원소만 포함

        - if BFS(A) and BFS(B): # BFS 가능 == 정상 그룹 형성 가능
            - a_total = A weights sum
            - b_total = B weights sum
            - ans = min(ans, abs(a_total - b_total))

- print(-1 if ans == INF else ans)

- comb(arr, r)

- BFS(group):
    - q = deque[(group[0])]
    - while queue:
        - for range(len(arr[node])):
            - if 이어지지 않음: 무시
            - if 그룹에 불포함 구역: 무시
            - if 미방문: queue 추가
    
    # 방문 총 횟수와 그룹 숫자가 동일해야 성립
    - return visited.count(True) == len(group) 

- get_total(arr):
    - for arr:
        - total += weights[node]

    - return total

'''

import sys
from collections import deque

input = sys.stdin.readline
def comb(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in comb(arr[i+1:], r-1):
                yield [arr[i]] + nxt

def BFS(group):
    queue = deque([group[0]])
    visited = [False for _ in range(N)]
    visited[group[0]] = True

    while queue:
        node = queue.popleft()
        for nnode in range(len(arr[node])):
            if not arr[node][nnode]:
                continue # 이어지지 않음
            if nnode not in group:
                continue # 그룹에 불포함 구역
            if not visited[nnode]: # 미방문시만 추가 탐색
                visited[nnode] = True
                queue.append(nnode)

    return visited.count(True) == len(group) # 방문 총 횟수와 그룹 숫자가 동일해야 성립


def get_total(arr):
    total = 0
    for node in arr:
        total += weights[node]

    return total

N = int(input()) # 구역의 개수 N
weights = list(map(int, input().split())) # 구역의 인구
arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    _, *districts = map(int, input().split()) # 그 구역과 인접한 구역의 수, 이후 인접한 구역의 번호
    for dst in districts:
        arr[i][dst - 1] = 1 # arr[정보번호][인접 구역 idx들] = 1

cases = []
nums = list(range(N))
INF = int(1e9)
ans = INF

for i in range(1, N // 2 + 1): # 절반 만큼만 테스트. 절반 이후 케이스는 R ~ B 그룹 바꾼 것과 동일.
    A_cases = tuple(comb(nums, i))
    for A in A_cases:
        B = list(set(nums).difference(A)) # nums 와 A 간 다른 원소만 표기

        if BFS(A) and BFS(B): # BFS로 둘다 가능하다면
            a_total = get_total(A) # weights sum 계산
            b_total = get_total(B)
            ans = min(ans, abs(a_total - b_total))

print(-1 if ans == INF else ans)