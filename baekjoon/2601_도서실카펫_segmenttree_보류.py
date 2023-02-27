import sys

input = sys.stdin.readline

class Node:
    def __init__(self, left, right, num):
        self.total = num
        self.max = num
        self.lazy = 0
        self.left = left
        self.right = right
        self.lc = None
        self.rc = None


class SegTree:
    def __init__(self, nums):
        if nums == []:
            return

        def build(left, right):
            if left == right:
                node = Node(left, right, nums[left])
                return node

            mid = left + right >> 1
            node = Node(left, right, 0)
            node.lc = build(left, mid)
            node.rc = build(mid + 1, right)
            node.max = max(node.lc.max, node.rc.max)
            return node

        self.root = build(0, len(nums) - 1)

    def propagation(self, node):
        if node.left != node.right:
            node.lc.lazy += node.lazy
            node.rc.lazy += node.lazy
        node.max += node.lazy
        node.lazy = 0
        return

    def query_range(self, left, right):
        def query_help(node, left, right):
            if node.left == node.right and node.left == left:
                if node.lazy != 0:
                    node.max += node.lazy
                    node.lazy = 0
                return node.max
            else:
                if node.lazy != 0:
                    self.propagation(node)
                if left <= node.left and node.left <= right:
                    return node.max
                elif right < node.left or node.right < left:
                    return 0
                else:
                    mid = node.left + node.right >> 1
                    a = query_help(node.lc, left, right)
                    b = query_help(node.rc, left, right)
                    node.max = max(node.lc.max + node.rc.max)
                    return max(a, b)

        return query_help(self.root, left, right)

    def update_range(self, left, right, value):
        def update_range_help(node, left, right, value):
            if node.left == node.right and node.left == left:
                if node.lazy != 0:
                    node.max += node.lazy
                    node.lazy = 0
                node.max += value
                return node.max
            else:
                if node.lazy != 0:
                    self.propagation(node)

                if left <= node.left and node.right <= right:
                    node.max += value

                    if node.left != node.right:
                        node.lc.lazy += value
                        node.rc.lazy += value
                    return node.max
                elif node.right < left or right < node.left:
                    return node.max
                else:
                    mid = node.left + node.right >> 1
                    node.max = max(update_range_help(node.lc, left, right, value),
                                   update_range_help(node.rc, left, right, value))
                    return node.max

        update_range_help(self.root, left, right, value)


_, height, width, _ = map(int, input().split()) # 전체 영역
c_w = int(input()) # 정사각형 카펫 가로길이
num_stain = int(input()) # 직사각형 개수
if num_stain == 0: # 직사각형 개수 0일 경우 0 출력 후 종료
    print(0)
    exit(0)
inputs = []
for _ in range(num_stain):
    try:
        x, y, xx, yy = map(int, input().split()) # 왼쪽 위, 오른쪽 아래 지점
        inputs.append((x, y, xx, yy))
    except ValueError:
        inputs.append(inputs[-1])

stains = list()
ys = set()
ys_idx = dict()
START, END = 0, 1
for i in range(num_stain):
    x, y, xx, yy = inputs[i]
    left = max(0, xx - c_w / 2)
    right = min(width, x + c_w / 2)
    upper = min(height, yy + c_w / 2)
    lower = max(0, y - c_w / 2)

    if left <= right:
        stains.append((left, lower, upper, START))
        stains.append((right, lower, upper, END))

        ys.add(upper)
        ys.add(lower)

ys = list(ys)
ys.sort()
for i, y in enumerate(ys):
    ys_idx[y] = i

stains.sort(key=lambda x: x[3])
stains.sort(key=lambda x: x[0])
nums = [0] * (len(ys))
st = SegTree(nums)
ans = 0
for x, lower, upper, t in stains:
    if t == START:
        st.update_range(ys_idx[lower], ys_idx[upper], 1)
    else:
        st.update_range(ys_idx[lower], ys_idx[upper], -1)
    maxv = st.query_range(0, len(ys) - 1)
    ans = max(ans, maxv)
print(ans)

