if __name__ == '__main__':
    N = int(input())
    res_lst = []
    for i in range(N):
        split = input().split()
        if "insert" in split:
            res_lst.insert(int(split[1]),int(split[2]))
        elif "print" in split:
            print(res_lst)
        elif "remove" in split:
            res_lst.remove(int(split[1]))
        elif "append" in split:
            res_lst.append(int(split[1]))
        elif "sort" in split:
            res_lst.sort()
        elif "pop" in split:
            res_lst.pop()
        elif "reverse" in split:
            res_lst.reverse()
