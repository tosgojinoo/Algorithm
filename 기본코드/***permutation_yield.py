# 순열
def perms(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in perms(arr[:i]+arr[i+1:], r-1): # i를 제외한 배열 대상으로 다시 perms
                yield [arr[i]] + nxt

for i in range(perms([1, 2, 3] , 2)):
    print(i)