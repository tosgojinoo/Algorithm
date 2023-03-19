'''
단순 반복문 가장 빠름
'''
def permutation(subset):
    if len(subset) == R:
        touch_list.append(subset)
        return
    for nxt in can_touch:
        nsubset = subset + [nxt]
        permutation(nsubset)

can_touch = list(range(10))
touch_list = []
R = 3 # 3번 선택
permutation(touch_list)
print(touch_list)
print(len(touch_list))