# 1
def combination(depth): # depth: 정해진 지점, beginWith: 이하 분석 지점
    if depth == R:
        result.append(picked[:])
        return
    for num in arr:
        picked.append(num) # 선정
        combination(depth+1)
        picked.pop() # 선정 제외

R = 3
arr = list(range(1, 6))

picked = []
result = []
combination(0)
print(result)
print(len(result))






'''
# 2
def dfs_comb2(subset, beginWith, R): # R: 남은 선택지
    if R == 0:
        result.append(subset)
        return

    for ni, nxt in enumerate(arr[beginWith:]):
        dfs_comb2(subset+[nxt], beginWith + ni + 1, R - 1)

result = []
dfs_comb2([], 0, R)
print(result)
'''