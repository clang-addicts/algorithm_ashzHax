def swap_case(s):
    ret = []
    for i in list(s):
        if i.isupper():
            ret.append(i.lower())
        elif i.islower():
            ret.append(i.upper())
        else:
            ret.append(i)
    return "".join(ret)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)