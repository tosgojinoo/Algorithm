def permutation(arr):
    N = len(arr)
    for flags in range(1<<N): # 2**N == 1<<N
        subarray = []
        for idx in range(N):
            if flags & (1 << idx):
                subarray += [arr[idx]]

        total_array.append(subarray)

total_array = []
arr = list(range(1, 5))
permutation(arr)
print(total_array)




# def permutation(arr):
#     N = len(arr)
#     for i in range(1<<N):
#         s = bin(i)[2:]
#         s = '0' * (N - len(s)) + s
#         print(list(map(int, list(s))))
#

# permutation(arr)