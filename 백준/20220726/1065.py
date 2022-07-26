#!/usr/env/python3

a = int(input())
cnt = 0

for i in range(1, a+1):
    # if num is smaller than 100, just add to counter
    if i < 100:
        cnt += 1
    else:
        flag = 1
        prev = -1
        diff = -1
        t = i

        # algorithm for AP on number over 100
        while t > 0:
            if prev < 0:
                prev = t % 10
                break

            if diff < 0:
                diff = prev - t % 10
                if diff < 0:
                    diff = diff * -1
                break
            
            print('debug: t:'+str(t)+' prev:'+str(prev)+' diff:'+str(diff)+' flag:'+str(flag))
            new_diff = (t % 10) - prev
            if new_diff < 0:
                new_diff *= -1
            if diff != new_diff:
                flag = 0
                break
            prev = t % 10
            t = int(t/10)
        if flag == 1:
            cnt += 1

print(cnt)