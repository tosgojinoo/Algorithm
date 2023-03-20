N, S = map(int, input().split())
T = list(map(int, input().split()))
A, B = T[:N//2], T[N//2:]
a, b = len(A), len(B)
tableA, tableB = {}, {}

def solution(n, sum_, i, o):
    if n == len(i):
        o[sum_] = o.get(sum_, 0)+1
        return
    solution(n+1, sum_, i, o)
    solution(n+1, sum_+i[n], i, o)

solution(0, 0, A, tableA)
solution(0, 0, B, tableB)

tableA[0] -= 1
tableB[0] -= 1

ans = tableA.get(S, 0) + tableB.get(S, 0)
for i in tableA:
    if S-i in tableB:
        ans += tableB[S-i] * tableA[i]
print(ans)