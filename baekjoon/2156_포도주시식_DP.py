'''
최대 2칸 포함, 1칸 이상 이격.
case
- DP(t-2) 제외한 DP(t-1) + now
- DP(t-1) 제외한 DP(t-2) + now
- now     제외한 DP(t-1))
'''
DP = [0]*3
N = int(input())
for _ in range(N):
    now = int(input())
    DP = DP[1] + now, DP[2] + now, max(DP) # (DP(t-2) 제외한 DP(t-1) + now , DP(t-1) 제외한 DP(t-2) + now, now 제외한 DP(t-1))
print(max(DP))