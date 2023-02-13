''' my idea
def is_available_paper(num):
    - for i in num:
        - if not num == 1
            return False
    return True

DFS(y, x, cnt, visited)
- 전체 탐색
- if x = y = N:
    - min(result, cnt)
    - return
- if 1 발견
    - for i in range(1,5+1):
        - if not is_available_paper(i)
            - continue
        - else:
            - 커버하면 cnt +=1
            - 커버한 모든 visited = 1
            - DFS(ny, nx, cnt, visited)
    - ...
    - if 5로 커버할 경우

'''

import sys

input = sys.stdin.readline


def find_length(y, x):
    length = 1
    for case in range(2, min(10 - y, 10 - x, 5) + 1): # 크기 5로 제한
        for i in range(y, y + case):
            for j in range(x, x + case):
                if arr[i][j] == 0: # 중간에 0이 있을 경우, 이전 사이즈를 return
                    return length
        length += 1
    return length



def cover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            arr[i][j] = 0


# 색종이 치우는 함수
def uncover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            arr[i][j] = 1


def DFS(cnt):
    for i in range(0, 10):
        for j in range(0, 10):
            if arr[i][j] == 1: # 1이면 계산
                max_length = find_length(i, j) # 최대 가능 길이
                for case in range(max_length, 0, -1):
                    if papers[case]: # 잔여분이 있다면
                        cover(i, j, case) # 색종이 덮고
                        papers[case] -= 1 # 감소
                        result.add(DFS(cnt + 1)) # 가능한 cnt 경우 저장
                        uncover(i, j, case) # arr 원복
                        papers[case] += 1 # 색종이 개수 원복
                if result:
                    return min(result)
                else:
                    return -1
    return cnt


arr = [list(map(int, input().split())) for _ in range(10)] # 크기 고정
papers = [0, 5, 5, 5, 5, 5] # paper_size = index * index
result = set()

result.add(DFS(0))

if -1 in result:
    result.remove(-1)
print(min(result) if result else -1)