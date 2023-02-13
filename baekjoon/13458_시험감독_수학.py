# N 개 시험장, A[i] 응시자
# 총감독관
#   - 한시험장당 B
# 부감독관
#   - 한시험장당 C
# i에는 1 총감독관, n 부감독관
# A[n] = B + C * x
# 처리시간 줄이려면, list comp. 사용하지 않고 바로 루프에서 모든 계산 처리

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

arr = [i-B if i-B >=0 else 0 for i in arr] # 뺀 값이 음수일 경우 0처리
# print(arr)
ans = len(arr)
if sum(arr) == 0:
    pass
else:
    for i, a in enumerate(arr):
        x, y = divmod(a, C)
        if y != 0:
            arr[i] = x+1
        else:
            arr[i] = x
    ans += sum(arr)

print(ans)
