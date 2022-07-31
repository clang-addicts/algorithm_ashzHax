# Enter your code here. Read input from STDIN. Print output to STDOUT
arr = input().split(' ')
y = int(arr[0])
x = int(arr[1])

for i in range(0, int(y/2)):
    print('-'*int((x/2)-(i*3)-1), end='')
    print('.|.'*(1+(i*2)), end='')
    print('-'*int((x/2)-(i*3)-1))

print('-'*(int((x-7)/2)), end='')
print('WELCOME', end='')
print('-'*(int((x-7)/2)))

for i in range(0, int(y/2)):
    t = int(y/2)-1 - i
    print('-'*int((x/2)-(t*3)-1), end='')
    print('.|.'*(1+(t*2)), end='')
    print('-'*int((x/2)-(t*3)-1))