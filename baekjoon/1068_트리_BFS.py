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

def BFS(idx_root):
    global result
    q = deque([idx_root])

    while q:
        node = q.popleft()
        if len(arr[node]) == 0: # 자식노드 조건
            result += 1

        for nnode in arr[node][::-1]: # pop 되면 다음 루프에 영향 주므로, 역순 입력
            q.append(nnode)
            arr[node].pop() # 뒤에서부터 pop

N = int(input())
arr_tmp = list(map(int, input().split()))
D = int(input())
arr = [[] for _ in range(len(arr_tmp))]
result = 0
idx_root = -1

for i in range(len(arr_tmp)):
    if arr_tmp[i] == -1:
        if i == D:
            break
        else:
            idx_root = i
    # 삭제 노드 반영
    elif arr_tmp[i] == D or i == D:
        continue
    else:
        arr[arr_tmp[i]].append(i)


# print(arr)
# print(idx_root)
if idx_root == -1:
    print(0)
else:
    BFS(idx_root)
    print(result)
# print(arr)


