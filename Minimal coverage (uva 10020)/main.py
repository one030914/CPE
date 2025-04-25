n = int(input())
for _ in range(n):
    ignore = input()
    m = int(input())
    l, r = [], []
    for _ in range(m):
        nums = tuple(input().split())
        l.append(nums[0])
        r.append(nums[1])