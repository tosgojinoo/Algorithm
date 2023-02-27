'''
DP의 idx 활용.
DP[idx == now_value] = 누적값.
'''

N = int(input())
arr = list(map(int, input().split()))
DP = [0] * 1001
for i in arr:
    DP[i] = max(DP[:i]) + i # DP의 idx 참고해 저장. 해당 숫자보다 작은 idx는 무시.
print(max(DP))