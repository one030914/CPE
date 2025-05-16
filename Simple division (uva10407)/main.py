def fun(a, b):
    return fun(b, a % b) if b else a

while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1 and nums[0] == 0:
        break
    nums = nums[:-1]
    ans = 0
    for i in range(1, len(nums)):
        ans = fun(ans, nums[i] - nums[i - 1])
    print(abs(ans))