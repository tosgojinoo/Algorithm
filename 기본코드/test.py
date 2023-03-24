def powerset(arr):
    N = len(arr)
    for flags in range(2**N):
        subarray = []
        for idx in range(N):
            if (flags >> idx) % 2 == 1:
                subarray += [arr[idx]]

        tot_array.append(subarray)

N = 5
arr = list(range(1, N+1))
tot_array = []
powerset(arr)
print(tot_array)
print(len(tot_array))