
def count_substring(string, sub_string):
    if len(string) < len(sub_string): 
        return 0
    flag = 0
    ret = 0
    j = 0
    main = list(string)
    sub = list(sub_string)
    for i in range(0,list(string)):
        j = 0
        while True:
            j += 1
            if i+j == len(string):
                break
            if j == len(sub_string):
                ret += 1
                break
    return ret

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)