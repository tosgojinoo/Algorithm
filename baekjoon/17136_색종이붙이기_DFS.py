'''
[설명]
정사각형 모양을 한 다섯 종류의 색종이
색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류
각 종류의 색종이는 5개씩
10×10인 종이 위에 붙이기
각각의 칸에는 0 또는 1
1이 적힌 칸은 모두 색종이로 덮기

- 색종이를 붙일 때
    - 종이의 경계 밖으로 나가서는 안됨
    - 겹쳐도 안 됨
    - 칸의 경계와 일치하게 붙이기
    - 0이 적힌 칸에는 색종이가 있으면 안 됨

[문제]
모든 1을 덮는데 필요한 색종이의 최소 개수 -> 최대 길이 -> DFS
1을 모두 덮는 것이 불가능한 경우에는 -1
'''
'''
[알고리즘]
- memory
    - papers 
        - idx: 색종이 한변 크기
        - value: 개수

- DFS
    - 색종이 덮을 최대 길이 계산(최소 개수 구하기 이므로, 최대 길이에서부터 역순으로 적용)
        - 색종이 덮기(0 처리)
        - papers --
        - result.add(DFS(색종이 개수+1))
        - 색종이 원복(1 처리)
        - papers ++

- find_length()
    - 최대 가능 길이 return
    - 범위를 넘어가지 않음, 최대 길이 5, (y,x)에서 가장 크게 뻗을 수 있는 한변 길이
        - min(10 - y, 10 - x, 5)
    - 위를 포함한 한변 길이의 범위
        - range(2, min(10 - y, 10 - x, 5) + 1)
    - 길이를 감안한 x의 범위
        - range(x, x + case)
'''
'''
[구조]
- arr 저장
- papers = [0, 5, 5, 5, 5, 5]
- result = set()

- result.add(DFS(0))

- if -1 in result:
    - result.remove(-1)
- print(min(result) if result else -1)

- DFS(cnt):
    - for 전체 탐색:
        - if arr[i][j]:
            - max_length = find_length(i, j)
            - for range(max_length, 0, -1):
                - if papers[case]: 잔여분 있음
                    - cover(i, j, case) 색종이 덮고
                    - papers[case] --
                    - result.add(DFS(cnt + 1)) # 가능한 cnt 경우 저장
                    - uncover(i, j, case) arr 원복
                    - papers[case] ++ # 색종이 개수 원복
            - if result:
                - return min(result)
            - else:
                - return -1
    - return cnt
    
- find_length(y, x):
    - length = 1
    - for range(2, min(10 - y, 10 - x, 5) + 1):
        - for range(y/x, y/x + case):
            - if 중간에 0이 있을 경우: 
                return length (이전 사이즈)
        - length ++
    - return length
    
- cover(y, x, length):
    - for range(y/x, y/x + length):
        - arr[i][j] = 0

- uncover(y, x, length):
    - for range(y/x, y/x + length):
        - arr[i][j] = 1

'''

import sys

input = sys.stdin.readline


def find_length(y, x):
    length = 1
    for case in range(2, min(10 - y, 10 - x, 5) + 1): # 크기 5로 제한
        for i in range(y, y + case):
            for j in range(x, x + case):
                if not arr[i][j]: # 중간에 0이 있을 경우, 이전 사이즈를 return
                    return length
        length += 1
    return length

def cover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            arr[i][j] = 0

def uncover(y, x, length):
    for i in range(y, y + length):
        for j in range(x, x + length):
            arr[i][j] = 1

def DFS(cnt):
    for i in range(10):
        for j in range(10):
            if arr[i][j]:
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


arr = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5] # paper_size = index * index
result = set()

result.add(DFS(0))

if -1 in result:
    result.remove(-1)
print(min(result) if result else -1)