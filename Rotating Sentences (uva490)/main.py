arr1 = []
arr2 = []
length = 0
while True:
    try:
        s = input()
        if length < len(s):
            length = len(s)
        arr1.append(s)
    except EOFError:
        for s in arr1:
            arr2.append(list(s.ljust(length, ' ')))
        arr2 = arr2[::-1]
        for i in range(length):
            for j in range(len(arr2)):
                print(arr2[j][i], end="")
            print()
        break