n = int(input())
flag = False
for _ in range(n):
    if flag: print()
    flag = True
    ignore = input()
    m = int(input())
    a, b = [], []
    for _ in range(m):
        nums = tuple(input().split())
        a.append(nums[0])
        b.append(nums[1])
    print(int(''.join(a)) + int(''.join(b)))