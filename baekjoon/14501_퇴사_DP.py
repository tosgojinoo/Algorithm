# DP
# Bottom-up, 시작 -> 끝
# 처음부터, 요소별 T만큼 떨어진 지점부터 끝까지 누적시킨 후 다음 요소를 택할 때와 비교하는 방식

N = int(input())
DP = [0]*99
for idx in range(1, N+1):
    DP[idx] = max(DP[idx-1], DP[idx])
    T, P = map(int, input().split()) # idx 는 T, DP[idx] 는 P
    DP[idx+T] = max(DP[idx+T], DP[idx]+P)
print(DP)
print(max(DP[N:N+2])) # N-1일까지 or N일 하루 포함 최대값


'''
import sys
input = sys.stdin.readline
N = int(input())

schedule = [list(map(int, input().split())) for i in range(N)]

DP = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i+schedule[i][0], N+1): # T가 N을 넘어가지 않는 경우만 저장. i의 해당 스캐줄 이후부터 P 적립. DP update는 N+1까지 해줘야함. DP[N+1] = DP[N] + P[N]
        if DP[j] < DP[i] + schedule[i][1]: # 이미 적립된 금액 보다 '새로운 금액+당시 적립 금액'이 크면 update
            DP[j] = DP[i] + schedule[i][1]

print(DP[-1])

# Top-down, 끝 -> 시작
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
DP = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if i + schedule[i][0] > N: # N 넘기면 제외
        DP[i] = DP[i+1]
    else:
        DP[i] = max(DP[i+1], schedule[i][1] + DP[i + schedule[i][0]]) # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택

print(DP[0])
'''