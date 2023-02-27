import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    DP = [[0] * n for _ in range(n)]
    chapters = list(map(int, input().split()))
    cum_sum = [0]
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = i
        cum_sum.append(cum_sum[i] + chapters[i]) # 누적합

    for z in range(1, n):
        for i in range(n-z): # DP 행렬의 윗 삼각형만 사용하기 위함. ex) z = 3, i = (0~1) | z = 1 , i = (0~3)
            j = i + z
            DP[i][j] = sys.maxsize

            # 기준값 k 탐색 구간 한정
            k_range_start = A[i][j - 1]
            k_range_end = min(A[i + 1][j] + 1, j) # range_end 값은 제외되기 때문에, 1 추가. or j 보다 작음.
            for k in range(k_range_start, k_range_end):
                minn = DP[i][k] + DP[k+1][j] + cum_sum[j+1] - cum_sum[i]
                if DP[i][j] > minn:
                    DP[i][j] = minn
                    A[i][j] = k # 채택한 기준값 저장

    print(DP[0][-1])
