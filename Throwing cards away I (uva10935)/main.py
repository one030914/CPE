while True:
    try:
        n = [int(_) for _ in input().split()]
        for i in n:
            if i == 0: break
            ar1 = [_ for _ in range(i, 0, -1)]
            ar2 = []

            while len(ar1) > 1:
                ar2.append(ar1.pop())
                ar1.insert(0, ar1.pop())
            print("Discarded cards:", ', '.join([str(_) for _ in ar2]))
            print("Remaining card:", ar1[0])
    except EOFError:
        break