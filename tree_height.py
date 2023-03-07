#Kristiāns Martiņjaks 221RDB223
import sys
import threading
def compute_height(n, ps):
    cs = [[] for _ in range(n)]
    for c, p in enumerate(ps):
        if p != -1:
            cs[p].append(c)
    def get_height(p):
        if not cs[p]:
            return 1
        else:
            return 1 + max(get_height(c) for c in cs[p])
    s = ps.index(-1)
    return get_height(s)
def main():
    while True:
        user_input = input("'I' for input, 'F' for file: ")
        if "I" in user_input:
            n = int(input())
            ps = list(map(int, input().split()))
            print(compute_height(n, ps))
            break
        elif "F" in user_input:
            path = './test/'
            file_name = input("File name: ")
            folder = path + file_name
            if 'a' in file_name:
                print("File can not contain letter 'a' ")
                break
            try:
                with open(folder, 'r', encoding='utf-8') as file:
                    n = int(file.readline())
                    ps = list(map(int, file.readline().split()))
                print(compute_height(n, ps))
                break
            except FileNotFoundError:
                print("File not found")
                break
            except ValueError:
                print("Invalid input format")
                break
        else:
            print("Type 'I' or 'F': ")
    print(compute_height(n, ps))
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()

