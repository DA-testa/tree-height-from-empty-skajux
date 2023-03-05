import sys
import threading
def compute_height(n, p):
    children = [[] for _ in range(n)]
    for child, parent in enumerate(p):
        if parent != -1:
            children[parent].append(child)
    def get_height(p):
        if not children[p]:
            return 1
        else:
            return 1 + max(get_height(child) for child in children[p])
    s = p.index(-1)
    return get_height(s)
def main():
    while True:
        user_input = input("'I' for input, 'F' for file: ")
        if "I" in user_input:
            n = int(input())
            p = list(map(int, input().split()))
            print(compute_height(n, p))
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
                    p = list(map(int, file.readline().split()))
                print(compute_height(n, p))
                break
            except FileNotFoundError:
                print("File not found")
                break
            except ValueError:
                print("Invalid input format")
                break
        else:
            print("Type 'I' or 'F': ")

        return 
    print(compute_height(n, parents))
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
