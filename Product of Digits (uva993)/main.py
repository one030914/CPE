import math

n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        print(10)
        continue
    elif num == 1:
        print(1)
        continue
    
    Q = []
    tmp = num
    for i in range(9, 1, -1):
        while(tmp % i == 0):
            tmp //= i
            Q.append(i)
    if len(Q) <= 0 or math.prod(Q) != num: print(-1)
    else:
        Q = ''.join(sorted(list(map(str, Q))))
        print(Q)