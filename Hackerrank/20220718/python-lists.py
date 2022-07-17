# https://docs.python.org/3/tutorial/datastructures.html
if __name__ == '__main__':
    N = int(input())

    cmd_arr = []
    arr = []
    for _ in range(0,N):
        cmd_arr.append(input().split(' '))

    for idx in cmd_arr:
        command = idx[0]
        if command == 'insert':
            arr.insert(int(idx[1]), int(idx[2]))
        elif command == 'print':
            print(arr)
        elif command == 'remove':
            arr.remove(int(idx[1]))
        elif command == 'append':
            arr.append(int(idx[1]))
        elif command == 'sort':
            arr.sort()
        elif command == 'pop':
            arr.pop()
        elif command == 'reverse':
            arr.reverse()
        else:
            print('unknow command: '+command)