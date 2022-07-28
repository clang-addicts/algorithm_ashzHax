if __name__ == '__main__':
    s = input()
    alpha = False
    numeric = False
    up = False
    low = False

    for a in s:
        if a.isalpha():
            alpha= True
        if a.isdigit():
            numeric = True
        if a.islower():
            low = True
        if a.isupper():
            up = True
    
    if alpha or numeric:
        print('True') 
    print(alpha)
    print(numeric)
    print(up)
    print(low)