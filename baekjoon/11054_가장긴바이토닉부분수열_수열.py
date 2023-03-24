input()
DP_up, DP_down = [0]*12, [0]*12
for num in list(map(int, input().split())):
   DP_up[num] = max(DP_up[:num])+1 # 수열에서 위치할 idx 입력
   DP_down[num] = max(max(DP_up[num+1:]), max(DP_down[num+1:]))+1 # 자신보다 큰 숫자 중 이전에 등장한 적이 있으면 +1
print(max(DP_down))