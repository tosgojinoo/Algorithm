def permutation(arr):
    N = len(arr)
    for i in range(1<<N):
        s = bin(i)[2:]
        s = '0' * (N-len(s)) + s
        print(list(map(int, list(s))))

arr = list(range(5))
permutation(arr)