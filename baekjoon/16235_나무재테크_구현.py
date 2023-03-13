'''
[설명]
N×N 크기
(r, c), r과 c는 1부터 시작 -> idx -1 shift
모든 칸에 대해서 양분 조사
처음에 양분은 모든 칸에 5만큼 -> init
M개의 나무
같은 1×1 크기의 칸에 여러 개의 나무가 심기 가능
- 사계절 과정 반복
    - 봄
        - 나무가 자신의 나이만큼 양분을 먹음 -> 양분 - 나이
        - 나이가 1 증가 -> 나이 ++
        - 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있음
        - 나이가 어린 나무부터 양분 먹음 -> 어린 나이부터 오름차순
        - 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽음 -> if 나이 > 양분: 죽음
    - 여름
        - 봄에 죽은 나무가 양분으로 변함 -> 양분으로 추가
        - 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가 -> 죽은 나무 나이 //2
        - 소수점 아래 생략
    - 가을
        - 번식
        - 번식하는 나무는 나이가 5의 배수 -> 나이%5 == 0
        - 인접한 8개의 칸에 나이가 1인 나무가 생김
        - 인접한 칸
            - (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) -> 주위 8 방향
        - 땅을 벗어나는 칸에는 나무가 생기지 않음 -> 범위 밖 무시
    - 겨울
        - 양분 추가
        - 추가 양분의 양은 A[r][c] -> arr_source 추가 관리
        - 입력으로 주어짐

[문제]
K년이 지난 후 살아남은 나무의 수를 출력 -> if cnt ~ K:
'''
'''
[알고리즘]
- tree 정보
    - {나무정보 (x, y, 나무 나이) : 나무개수(초기값 1)}
    -

- 4계절 한번에 계산
- 양분 기준
    - 봄(소모) > 여름(추가) > 가을(-) > 겨울(추가)
    - 순서 변경: 겨울 > 봄 > 여름 > 가을
- solve()
    - 여름에 죽어서 변한 양분은 그 다음해 봄에 소비
    - 그러므로, 어린 나무 순으로, 나무별 4계절을 우선 계산
    - for sorted({x, y, 나이}.items, key=lambda x[0][2])
        - 양분의 합 source를 따로 변수 저장하지 않으면 시간 초과 발생
        - 겨울(양분추가) > 봄 > 여름(사망) > 가을 > 여름(양분추가) 순서
        - 4계절 조건에 따라 계산
        - add_tree()
- add_tree()
    - tree_list에 추가 
- print(sum(tree.values()))    
'''
'''
[구조]
- arr, arr_source 저장
- tree dict() 저장
- solve
    - for 나무 정보, 나이 어린순 오름차순:
        - [겨울] source = arr + arr_source
        - if [봄] 양분 조건, 나이
            - if 양분 조건, 개수:
                - 양분 소모 or not
            - if [가을] 나이 조건
                - 번식 > add_tree(new_tree)
        - else 
            - [여름] 사망 > add_tree(dead_tree) 

    - for [여름] (정산된) dead_tree:
        - 양분화
    - return new_tee
- print(sum(tree.values()))    
'''


'''



'''

import sys
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
add_source = [list(map(int, input().split())) for _ in range(n)] # 추가 양분값
tree = {tuple(map(int, input().split())): 1 for _ in range(m)} # {나무정보 (x, y, 나무 나이) : 나무개수(초기값 1)}

for i in range(k): # 매해 결과 계산
    tree = solve(tree, i)

print(sum(tree.values()))