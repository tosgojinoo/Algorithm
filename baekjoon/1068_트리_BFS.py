# 노드 삭제 시 자식노드 모두 삭제
# 리프 노드 구하기
# 루트 == -1

# 순서
# 입력 > 트리 구성
# -'삭제 노드'를 포함한 정보일 경우 삭제
# 루트 노드 (-1)부터 탐색
# 리프 노드 감별
# - 더이상 진전이 없을 경우
# 리프노드일 경우 리프노드 출력

# 제한
# bfs, dfs 무관 > (변경) DFS 가 두배 빠름
# 루트가 복수개일 경우 <- 이런 경우 없음
# ***** 루트를 삭제했을 경우, 0으로 출력

# 체크

from collections import deque
import sys
input = sys.stdin.readline # 입력 신경쓰기

def BFS():
    global result
    queue = deque([idx_root])

    while queue:
        node = queue.popleft()
        if len(arr[node]) == 0: # 자식노드 조건. 루프 전 확인 필수. node1이 삭제되고 루트만 남았을 경우를 위해
            result += 1
        for nnode in arr[node]:
            queue.append(nnode)

N = int(input())
arr_tmp = list(map(int, input().split()))
D = int(input())
arr = [[] for _ in range(len(arr_tmp))]
result = 0
idx_root = -1

for i in range(len(arr_tmp)):
    if arr_tmp[i] == -1: # root 면
        if i == D: # root(0) 가 삭제 대상이면, 종료
            break
        else:
            idx_root = i
    # 삭제 노드 반영
    elif arr_tmp[i] == D or i == D: # 부모 node or 자신이 삭제 대상이면 무시
        continue
    else:
        arr[arr_tmp[i]].append(i) # arr[node] = 자식 node 형태 재구성

if idx_root == -1:
    print(0) # 0이 삭제 대상
else:
    BFS()
    print(result)
# print(arr)


