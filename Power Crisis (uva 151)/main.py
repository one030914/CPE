while True:
    try:
        n = [int(_) for _ in input().split()]
        for i in n:
            if i == 0: break
            m = 1
            while True:
                ar1 = list(range(1, i + 1))
                while len(ar1) > 1:
                    ar1.pop(0)
                    for _ in range(m - 1):
                        a = ar1.pop(0)
                        ar1.append(a)
                if ar1[0] == 13: break
                m += 1
            print(m)
    except EOFError:
        break