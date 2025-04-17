from collections import defaultdict

n = int(input())
d = defaultdict(lambda: 0)

for _ in range(n):
    line = [_.upper() for _ in input() if 91 > ord(_.upper()) > 64]
    for c in line:
        d[c] += 1

d = dict(sorted(d.items(), key=lambda x: (-x[1], x[0])))
for i, j in d.items():
    print(f"{i} {j}")