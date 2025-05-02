from collections import Counter

while True:
    try:
        a = list(input().rstrip())
        b = list(input().rstrip())
        c = ''.join(sorted(list((Counter(a) & Counter(b)).elements())))
        print(c)
    except EOFError:
        break
