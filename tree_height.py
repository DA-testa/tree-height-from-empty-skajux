# python3

import sys
import threading

def compute_height(n, parents):
    children = [[] for i in range(n)]
    root_index = -1
    for i in range(n):
        parent_index = parents[i]
        if parent_index == -1:
            root_index = i
        else:
            children[parent_index].append(i)
    def compute_subtree_height(node_index):
        if not children[node_index]:
            return 1
        else:
            child_heights = [compute_subtree_height(child_index) for child_index in children[node_index]]
            return max(child_heights) + 1
    return compute_subtree_height(root_index)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
