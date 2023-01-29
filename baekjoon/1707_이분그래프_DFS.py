# 이분 그래프 (Bipartite Graph)
# https://hongcoding.tistory.com/20
# - 그래프의 정점의 집합을 둘로 분할
# - 각 집합에 속한 정점끼리는 서로 인접하지 않도록
# (추가) 정점을 두가지 색 그룹으로 분리할 때, 인접한 정점끼리는 다른색인 그래프

# 순서
# 1) 리스트 생성 및 edge 입력
# 2) 1번 idx 부터 정점 v 따라감
# 3) 정점 v와 연결된 target들에 대해 탐색
# 4) visited 에 0(미방문), 1(방문, group1), -1(방문, group2) 표기
# 5) 종료조건 확인

# 종료 조건
# 1) No
#   - 방문 했는데, 이전 노드와 같은 group 일 경우
#   - 미 방문하여 확인했더니, 이분그래프를 충족하지 않을 경우
# 2) 모든 idx 탐색 후 No가 아니면, Yes

# 두 그룹으로 나누는 경우, group 처리를 1, -1로 하고, 방문 여부는 0으로 처리
# input을 sys 처리 안해주면 시간초과 발생

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(v, group):
    # global visited
    visited[v] = group
    for target in arr[v]:
        # 미방문 & 이분그래프x
        if visited[target] == 0 and not DFS(target, -group):
            return False
        # 방문 했는데 동일 그룹일 경우
        elif visited[target] == visited[v]:
            return False
    return True

K = int(input()) # test case
for tc in range(K):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        idx, target = map(int, input().split())
        arr[idx].append(target)
        arr[target].append(idx)

    for i in range(1, V+1):
        if visited[i] == 0:
            bipatite = DFS(i,1)
            if not bipatite:
                break

    print("NO" if not bipatite else "YES")
