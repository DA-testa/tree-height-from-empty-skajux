import sys
import threading
def compute_height(n, parents):
    children = [[] for i in range(n)]
    root_index = parents.index(-1)
    for i in range(n):
        if parents[i] != -1:
            children[parents[i]].append(i)
    def compute_subtree_height(node_index):
        if not children[node_index]:  
            return 1
        else:  
            subtree_heights = [compute_subtree_height(child_index) for child_index in children[node_index]]
            return 1 + max(subtree_heights)
    return compute_subtree_height(root_index)
def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
sys.setrecursionlimit(10**6)
threading.stack_size(2**27)
thread = threading.Thread(target=main)
thread.start()
