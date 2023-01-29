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