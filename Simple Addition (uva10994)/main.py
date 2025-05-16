def fun(n):
    sum = 0
    while n > 0:
        sum += (n // 10) * 45 + (n % 10 + 1) * (n % 10) // 2
        n //= 10
    return sum

while True:
    n = list(map(int, input().split()))
    for i in range(0, len(n), 2):
        p, q = n[i], n[i + 1]
        if p == -1 and q == -1:
            break
        
        print(fun(q) - fun(p - 1))
    if p == -1 and q == -1:
        break
