'''
[양분 기준]
봄(소모) - 여름(추가) - 가을(-) - 겨울(추가)
[순서 변경]
겨울 - 봄 - 여름 - 가을
[구조]
for 나무 정보:
    [겨울] 조건
    if [봄] 조건
        양분 소모
    if [가을] 조건
        번식
        
for [여름] (정산된) 죽은 나무 정보:
    양분화
'''

import sys
from collections import defaultdict
input = sys.stdin.readline

def add_tree(y, x, age, cnt, tree_list):
    if (y, x, age) in tree_list:
        tree_list[(y, x, age)] += cnt
    else:
        tree_list[(y, x, age)] = cnt

def solve(tree, k):
    # 4계절 한번에 계산
    new_tree = dict()
    dead_tree = dict()
    for (y, x, age), cnt in sorted(tree.items(), key=lambda x: x[0][2]): # 나이가 가장 적은 나무부터 오름차순으로 확인
        source = arr[y-1][x-1] + add_source[y-1][x-1]*k # 겨울. x/y 시작이 1부터 이므로, 0 기준으로 변환.
        if source >= age: # 봄. 양분이 자신의 나이보다 많아야 생존.
            if source // age >= cnt: # 나무수 cnt 만큼 양분이 충분한가.
                arr[y-1][x-1] -= age*cnt # 양분 소비
                age += 1 # 소비 후 나이 증가
                add_tree(y, x, age, cnt, new_tree)
            else: # 양분 부족으로 일부만 생존
                arr[y-1][x-1] -= (source // age) * age # age의 정수배 만큼만 양분 소비
                add_tree(y, x, age, cnt - source // age, dead_tree) # 죽을 나무 반영
                cnt = source // age # 감소분 만영
                age += 1
                add_tree(y, x, age, cnt, new_tree) # 감소된 신규 나무 반영
            if age % 5 == 0: # 가울. 5의 배수만 대상. 인접 8칸에 나이 1인 나무 생성.
                for dy, dx in direction:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny-1 < n and 0 <= nx-1 < n: # 범위 내
                        add_tree(ny, nx, 1, cnt, new_tree) # 신규 나무 추가
        else: # 양분 부족으로 사망.
            add_tree(y, x, age, cnt, dead_tree)
    for (y, x, age), cnt in dead_tree.items(): # 여름. 죽은 나무 양분화
        arr[y-1][x-1] += (age//2) * cnt # 양분으로 추가
    return new_tree


direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)] # 8방향.
n, m, k = map(int, input().split()) # 배열 크기, 나무 정보 개수, 년수
arr = [[5 for _ in range(n)] for _ in range(n)] # 양분. 초기값 5.
add_source = [list(map(int,input().split())) for _ in range(n)] # 추가 양분값
tree = {tuple(map(int,input().split())): 1 for _ in range(m)} # {나무정보 (x, y, 나무 나이) : 나무개수(초기값 1)}

for i in range(k): # 매해 결과 계산
    tree = solve(tree, i)

print(sum(tree.values()))