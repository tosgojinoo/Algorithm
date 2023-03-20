'''
가장 빠름
'''
arr = list(range(1, 5))
subsets = [[]] # 공집합만 추가

for num in arr:
    for idx in range(len(subsets)): # len(subsets) 점점 증가
        subsets.append(subsets[idx] + [num])

print(subsets)