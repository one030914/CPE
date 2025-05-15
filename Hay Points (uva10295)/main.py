m, n = map(int, input().split())
d = dict()
for _ in range(m):
    w, p = input().split()
    d[w] = int(p)
for _ in range(n):
    text = ""
    while True:
        line = input()
        text += line + " "
        if '.' in text:
            break
    text = text.split()
    price = 0
    for word in text:
        if word in d:
            price += d[word]
    print(price)