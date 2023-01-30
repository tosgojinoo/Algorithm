"""
- class로 node만 생성
- 단순 카운팅이므로, recursive
- 시작점을 0으로 하고, 이후부터 1씩 증가
- 좌우 분할 정복하여, 둘 중 최대값을 계산하고, 최종 노드에서 합치기

         3
        /\
       2  5
      /   \
     9    10
diameter = 5
         3
        /\
       2  5
      / \  \
     9  8  10
         \
         4
diameter = 6
"""


class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


def diameter(node):
    if not node:
        return 0
    left_diameter = longest_path(node.left)
    right_diameter = longest_path(node.right)
    return left_diameter + right_diameter + 1


def longest_path(node):
    if not node:
        return 0

    left = longest_path(node.left)
    right = longest_path(node.right)

    return max(left, right) + 1


head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.left.left = Node(9)
head.right.right = Node(10)

print(diameter(head))

head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.left.left = Node(9)
head.left.right = Node(8)
head.right.right = Node(10)
head.left.right.right = Node(4)

print(diameter(head))

print(diameter(None))
print(diameter(Node(10)))