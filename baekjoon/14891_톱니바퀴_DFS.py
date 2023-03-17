'''
[설명]
8개의 톱니를 가지고 있는 톱니바퀴, 4개가 일렬
톱니는 N극 또는 S극 중 하나
톱니바퀴에는 번호
가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번
톱니바퀴를 총 K번 회전
톱니바퀴의 회전은 한 칸을 기준
회전은 시계 방향과 반시계 방향
톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정

- 톱니바퀴 A를 회전할 때,
    - 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면 -> 탐색 DFS
        - B는 A가 회전한 방향과 반대방향으로 회전

첫째 줄에 1번 톱니바퀴의 상태
둘째 줄에 2번 톱니바퀴의 상태
셋째 줄에 3번 톱니바퀴의 상태
넷째 줄에 4번 톱니바퀴의 상태
상태는 8개의 정수
12시방향부터 시계방향 순서대로
N극은 0, S극은 1

다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)
다음 K개 줄에는 회전시킨 방법
각 방법은 두 개의 정수
첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향
방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

- 점수 계산
    - 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
    - 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
    - 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
    - 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점

[문제]
K번 회전시킨 이후에 네 톱니바퀴의 점수의 합
'''
'''
[알고리즘]

- rotate_clock(), rotate_ban_clock()
    - gear 배열 순서 변경

- DFS(gear_idx, dir)
    - gear_idx 방문 처리
    - 3, 9시 방향 톱니 상태 확인
    - dir 적용
    - 옆 톱니의 반대방향 회전 조건 > 왼쪽/오른쪽 확인 > DFS(idx+1)
'''
'''
[구조]
- arr 톱니배열 저장
data = []

- for range(회전횟수 k):
    - gear_idx, dir = map(int, input().split()) # 톱니바퀴 번호, 방향
    - visited = [0] * 4
    - DFS(gear_idx - 1, dir) # gear_idx -1 shift

- for 톱니:
    - if 12시방향 N극:
        - cnt += (2**i) # 문제 조건
- print(cnt)


- DFS(gear_idx, dir):
    if 미방문:
        - visited[gear_idx] = 방문처리
        - left = arr[gear_idx][6] # 9시 방향
        - right = arr[gear_idx][2] # 3시 방향
        
        - if dir == 시계 방향:
            - rotate_clock(arr[gear_idx])
        - else:
            - rotate_ban_clock(arr[gear_idx])
        
        # 옆 톱니의 반대방향 회전 조건
        # 왼쪽 톱니 존재 조건. 왼쪽 톱니의 3시 방향의 극이 다른지.
        - if gear_idx-1 >= 0 and left != arr[gear_idx-1][2]: 
            - DFS(gear_idx - 1, -dir) # 반대방향
        # 오른쪽 톱니 존재 조건. 오른쪽 톱니의 9시 방향의 극이 다른지.
        - if gear_idx+1 <= 3 and right != arr[gear_idx+1][6]: 
            - DFS(gear_idx + 1, -dir) # 반대방향

- rotate_clock(arr):
    - arr[1:], arr[0] = arr[:-1], arr[7] # 시계방향이므로 1칸씩 뒤로 이동

- rotate_ban_clock(arr):
    - arr[:-1], arr[7] = arr[1:], arr[0] # 반시계방향이므로 1칸씩 앞으로 이동
'''

import sys
input = sys.stdin.readline


def rotate_clock(arr):
    arr[1:], arr[0] = arr[:-1], arr[7] # 시계방향이므로 1칸씩 뒤로 이동

def rotate_ban_clock(arr):
    arr[:-1], arr[7] = arr[1:], arr[0] # 반시계방향이므로 1칸씩 앞으로 이동

def DFS(gear_idx, dir):
    global visited
    if not visited[gear_idx]:
        visited[gear_idx] = 1
        left = arr[gear_idx][6] # 9시 방향
        right = arr[gear_idx][2] # 3시 방향
        if dir == 1: # 시계 방향
            rotate_clock(arr[gear_idx])
        else:
            rotate_ban_clock(arr[gear_idx])
        if gear_idx-1 >= 0 and left != arr[gear_idx-1][2]: # 왼쪽 있는지 확인. 왼쪽 톱니의 3시 방향의 극 확인.
            DFS(gear_idx - 1, -dir) # 반대방향
        if gear_idx+1 <= 3 and right != arr[gear_idx+1][6]: # 오른쪽 있는지 확인. 오른쪽쪽 톱니의 9시 방향의 극 확인.
            DFS(gear_idx + 1, -dir) # 반대방향


arr = [list(input().strip()) for _ in range(4)] # 톱니배열
k = int(input()) # 회전 횟수
data = []

for _ in range(k):
    gear_idx, dir = map(int, input().split()) # 톱니바퀴 번호, 방향
    visited = [0] * 4
    DFS(gear_idx - 1, dir) # 톱니가 1부터 시작함.

cnt = 0
for i in range(4):
    if arr[i][0] == '1': # 12시방향의 극만 확인 후 점수 계산
        cnt += (2**i)
print(cnt)