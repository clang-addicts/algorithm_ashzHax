if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    mr = []
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                t = i+j+k
                if t == n:
                    continue;
                tr = [i,j,k]
                mr.append(tr)
    print(mr)