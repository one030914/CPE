def b2d(n):
    d = 0
    for i in n:
        d = (d * 2 + int(i)) % 131071
    return d == 0
while True:
    try:
        bits = ""
        while True:
            line = input()
            bits += line
            while '#' in bits:
                chunk, bits = bits.split('#', 1)
                print("YES" if b2d(chunk) else "NO")
    except EOFError:
        break