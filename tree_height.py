class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(n, parents):
    nodes = [Node(i) for i in range(n)]

    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])

    return root

def calculate_height(node):
    if not node.children:
        return 1

    max_height = 0
    for child in node.children:
        height = calculate_height(child)
        max_height = max(max_height, height)

    return max_height + 1

n = int(input())
parents = list(map(int, input().split()))

tree = build_tree(n, parents)
height = calculate_height(tree)

print(height)
