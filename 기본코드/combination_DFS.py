# 1
def comb(now, end, start): # now: 정해진 지점, start: 이하 분석 지점
    if now == end:
        result.append(picked.copy())
        return
    for i in range(start, len(data)): # now >= start
        # 선정
        picked.append(data[i])
        comb(now+1, end, i+1)
        # 선정 제외
        picked.pop()

N, M = 5, 3
data = range(1, N+1)
picked = []
result = []

comb(0, M, 0)
print(result)
print(len(result))

# 2
def comb(n, r):
  if r == 0: return
  elif n < r: return
  else:
    tr[r-1] = data[n-1]
    if None not in tr:
      result.append(tr.copy())
    comb(n-1, r-1) # r번째 포함된 경우
    comb(n-1, r) # r번째 불포함 경우

data = input() # n개의 대상 리스트
n, r = len(data), input()
result = []
tr = [None for _ in range(r)] # 조합 임시 저장 리스트
comb(n, r)
print(result)

# 3
data = range(1,5+1)
visited = [False] * len(data)
pickednum = []
result = []

def comb(cnt, depth, beginWith): # level_now, level_final, start
	if cnt == depth:
		result.append(pickednum.copy())
		return
	for index in range(beginWith, len(data)):
		pickednum.append(data[index])
		comb(cnt+1, depth, index+1)
		pickednum.pop()

comb(0,3,0)