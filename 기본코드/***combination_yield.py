# 조합 (중복x)
def combination(arr, r):
    for i in range(len(arr)):
        if r == 1: # 종료 조건
            yield [arr[i]]
        else:
            for nxt in combination(arr[i+1:], r-1):
                yield [arr[i]] + nxt