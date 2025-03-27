while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break

    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(max(len(a), len(b)))

    carry = 0
    carry_count = 0

    for i in range(len(a) - 1, -1, -1):
        total = int(a[i]) + int(b[i]) + carry
        if total >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0

    if carry_count == 0:
        print("No carry operation.")
    elif carry_count == 1:
        print("1 carry operation.")
    else:
        print(f"{carry_count} carry operations.")
