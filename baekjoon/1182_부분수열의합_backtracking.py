import sys

def back_tracking(idx, subarr):
    global cnt

    # 현재 idx가 정수의 개수보다 크면 리턴
    if idx >= N:
        return

    # 수열에 현재 idx 정수를 더한다.
    subarr += arr[idx]

    # 현재 수열이 s라면 카운트
    if subarr == S:
        cnt += 1

    back_tracking(idx + 1, subarr) # 현재 idx 정수를 더한 것
    back_tracking(idx + 1, subarr - arr[idx]) # 현재 idx 정수를 더하지 않은 것(백트래킹)


N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0

back_tracking(0, 0)
print(cnt)