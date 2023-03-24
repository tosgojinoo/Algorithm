'''
처음부터 집다가, 100에 가장 가까운 지점에서 멈추기
'''
cum_sum = 0
gap_before = 99
for i in range(10): # 10개 고정
    cum_sum += int(input())
    gap_now = abs(100-cum_sum)
    if gap_now > gap_before:
        break
    gap_before = gap_now
    result = cum_sum
print(result)