# def powerset():
#     for i in range(2**N):
#         flag = bin(i)[2:].zfill(N)
#         subset = [data[j] for j in range(N) if flag[j] == '1']
#         result.append(subset)

'''
def DFS(now, end, limit): # limit 개수 이하 전부 뽑기, 순서 무시
    global picked
    # 기본 조건
    if (now==end+1):
        # 추가 조건
        if 0< len(picked) <= limit:
            result.append(picked)
        return        
    else:
        if visited[now] == 0:
            visited[now]=1
            picked.append(data[now])
            picked = picked[:-1]
            DFS(now+1, end, limit)
            visited[now]=0

N = 6
data = range(1,N+1)
visited = [0]*(N) # 체크 변수
picked = []
result = []
DFS(0, N-1, 3)
for r in result:
    print(r)
# print(len(result))
'''

def DFS(now, end, limit): # limit 개수 이하 전부 뽑기, 순서 무시
    global picked
    # 기본 조건
    if (now==end+1):
        # 추가 조건
        if 0< len(picked):
            result.append(picked)
        return        
    else:
        if visited[now] == 0:
            visited[now]=1
            picked.append(data[now])
            if len(picked) <= limit:
                DFS(now+1, end, limit)
            picked = picked[:-1]
            DFS(now+1, end, limit)
            visited[now]=0

N = 6
data = range(1,N+1)
visited = [0]*(N) # 체크 변수
picked = []
result = []
DFS(0, N-1, 3)
for r in result:
    print(r)
# print(len(result))









# 부분집합 기본코드
def printSet(n):
    for i in range(n):
        if A[i] == 1:
            print(data[i], end=" ")
    print()


# 부분집합의 합
def powerset(k, n, sum):
    if sum > 10:  # 부분집합의 합을 구하는 문제에서 구하고자하는 값인 10을 넘는다면 더이상 계산할 필요가 없으므로 return해버린다.(가지치기)
        return
    if n == k:
        printSet(k, sum)
    else:
        A[k] = 1
        powerset(k + 1, n, sum + data[k])
        A[k] = 0
        powerset(k + 1, n, sum)


data = "구하려는 리스트"
n = len(data)  # 부분집합을 구하는 리스트의 수
A = [0] * n  # 포함 유무를 체크할 리스트 (0이 미포함, 1이 포함)

