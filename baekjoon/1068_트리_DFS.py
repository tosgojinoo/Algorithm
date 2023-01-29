import sys
input = sys.stdin.readline

def DFS(node):
    global arr, result
    if len(arr[node]) == 0: # 자식노드 조건
        result += 1
        return

    for nnode in arr[node]:
        DFS(nnode)

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

if idx_root == -1:
    print(0)
else:
    DFS(idx_root)
    print(result)

