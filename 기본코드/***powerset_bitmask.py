'''
각 원소마다 분기점을 나누기 때문에 O(2^n)의 시간복잡도를 가짐
따라서 n이 큰 경우에는 시간초과가 나지 않도록 적절히 가지치기 필요함
N < 20 에서만 사용
'''
def powerSet(items):
    N = len(items)
    outer_combo = []
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        inner_combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                inner_combo.append(items[j])
        # options
        # if len(inner_combo) > 2:

        outer_combo.append(inner_combo)
    return outer_combo


a = list(range(20))
print(powerSet(a))



