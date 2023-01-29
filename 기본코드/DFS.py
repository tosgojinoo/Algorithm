# def DFS(now, end, limit): # limit 개수만큼 뽑기
#     global picked
#     # 기본 조건
#     if now==end+1:
#         # 추가 조건이 있다면 추가
#         return
#     if len(picked) == limit:
#         result.append(picked.copy())            
#     else:
#         if visited[now] == 0:
#             visited[now]=1
#             picked.append(data[now])
#             DFS(now+1, end, 3)
#             picked = picked[:-1]
#             DFS(now+1, end, 3)
#             visited[now]=0

def DFS(now, end, limit): # limit 개수 이하 전부 뽑기
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
