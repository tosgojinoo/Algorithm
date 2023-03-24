'''
각 원소마다 분기점을 나누기 때문에 O(2^n)의 시간복잡도를 가짐
따라서 n이 큰 경우에는 시간초과가 나지 않도록 적절히 가지치기 필요함
N < 20 에서만 사용
'''
def powerset(arr):
    N = len(arr)
    for flags in range(2**N):
        subarray = []
        for idx in range(N):
            if (flags >> idx) % 2 == 1:
                # print(f'bin(flags): {bin(flags)}, bin((flags >> idx)): {bin((flags >> idx))}')
                subarray += [arr[idx]]
        # options
        # if len(subarray) > 2:

        total_array.append(subarray)

total_array = []
a = list(range(1, 6))
powerset(a)
print(total_array)
print(len(total_array))


