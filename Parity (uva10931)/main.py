while True:
    n = int(input())
    if n == 0: break
    m = n
    s = ''
    while n > 1:
        m = n % 2
        s += str(m)
        n //= 2
    s += str(n)
    s = [int(_) for _ in s]
    c = sum(s)
    s = ''.join([str(_) for _ in s][::-1])
    print(f"The parity of {s} is {c} (mod 2).")