#!/usr/env/python3
# possibile recursive mathmatics?

a = int(input())
cnt = 0

for i in range(1, a+1):
    # if num is smaller than 100, just add to counter
    if i < 100:
        cnt += 1
    else:
        flag = 1
        prev = 10
        diff = 10
        t = i

        # algorithm for AP on number over 100
        while t > 0:
            now = t % 10
            if prev >= 10:
                prev = now
                t = int(t/10)
                continue

            if diff >=10:
                diff = prev - now
#                if diff < 0:
#                    diff = diff * -1
                prev = now
                t = int(t/10)
                continue
            
#            print('debug: t:'+str(t)+' prev:'+str(prev)+' diff:'+str(diff)+' flag:'+str(flag))
            new_diff = prev - now
#            if new_diff < 0:
#                new_diff *= -1
#            print('debug: new_diff:'+str(new_diff))
            if diff != new_diff:
                flag = 0
                break

            prev = now
            t = int(t/10)
        if flag == 1:
            #print('incr: '+str(i))
            cnt += 1

print(cnt)