import sys

sys.setrecursionlimit(10**6)

def compute_height(n, parents):
    tree = {}
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            if parents[i] not in tree:
                tree[parents[i]] = []
            tree[parents[i]].append(i)
    def compute_height_helper(node):
        if node not in tree:
            return 0
        else:
            heights = [compute_height_helper(child) for child in tree[node]]
            return max(heights) + 1
    return compute_height_helper(root)
n = int(input())
parents = list(map(int, input().split()))
print(compute_height(n, parents))
