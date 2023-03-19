def powerset(arr):
    if len(arr) <= 1:
        yield arr
        yield []
    else:
        for nxt in powerset(arr[1:]):
            yield [arr[0]] + nxt
            yield nxt

for i in powerset([1,2,3,4,5]):
    if len(i) <= 3:
        print(i)