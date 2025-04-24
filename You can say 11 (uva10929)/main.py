while True:
    num = input()
    if num == '0': break
    nums = list(map(int, list(num)))
    odd = sum(nums[i] for i in range(0, len(nums), 2))
    even = sum(nums[i] for i in range(1, len(nums), 2))
    if abs(odd - even) % 11 == 0:
        print(f"{num} is a multiple of 11.")
    else:
        print(f"{num} is not a multiple of 11.")