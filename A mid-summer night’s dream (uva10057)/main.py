while True:
    try:
        n = int(input())
        nums = []
        for _ in range(n):
            nums.append(int(input()))
        nums.sort()
        if n % 2 == 0:
            mid1 = nums[n // 2 - 1]
            mid2 = nums[n // 2]
            nx = sum([1 for i in nums if i == mid1 or i == mid2])
            np = mid2 - mid1 + 1
        else:
            mid1 = nums[n // 2]
            nx = sum([1 for i in nums if i == mid1])
            np = 1
        print(mid1, nx, np)
    except EOFError:
        break