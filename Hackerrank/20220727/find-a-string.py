def count_substring(string, sub_string):
    if len(string) < len(sub_string): 
        return 0
    flag = 0
    ret = 0
    j = 0
    main = list(string)
    sub = list(sub_string)
    for i in range(0,len(string)):
        j = 0
        flag = 1
        while j < len(sub_string):
            if i+j >= len(string):
                flag = 0
                break

            #print('compare: main[i+j]'+main[i+j])
            #print('compare: sub['+str(j)+'] '+sub[j])

            if main[i+j] != sub[j]:
                flag = 0
                break
            j += 1
        if flag == 1:
            ret += 1
    return ret

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)