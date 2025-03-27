def get_9_degree(n_str):
    degree = 0
    if n_str == '9':
        return degree + 1
    while len(n_str) > 1:
        n_str = str(sum(int(d) for d in n_str))
        degree += 1
    return degree

while True:
    num = input()
    if num == '0':
        break

    if sum(int(d) for d in num) % 9 != 0:
        print(f"{num} is not a multiple of 9.")
    else:
        deg = get_9_degree(num)
        print(f"{num} is a multiple of 9 and has 9-degree {deg}.")