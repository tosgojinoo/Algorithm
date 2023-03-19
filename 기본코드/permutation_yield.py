# 순열
def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in permutation(arr[:i]+arr[i+1:], r-1): # i를 제외한 배열 대상으로 다시 permutation
                yield [arr[i]] + nxt

print(list(permutation([1,2,3], 3)))