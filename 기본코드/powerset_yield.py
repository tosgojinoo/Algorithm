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



def powerSet(items):
    # generate all combinations of N items, items is a Python list
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

a = list(range(5))
print(list(powerSet(a)))