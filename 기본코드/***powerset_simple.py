'''
가장 빠름
'''
arr = list(range(22))
subsets = [[]]

for num in arr:
    size = len(subsets)
    for y in range(size):
        subsets.append(subsets[y]+[num])
print(subsets)