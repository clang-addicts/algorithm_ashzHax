if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    s=-100
    h=-100
    for i in arr:
        if i==h:
            continue
        if i>h:
            s=h
            h=i
        elif i>s:
            s=i
    print(s)