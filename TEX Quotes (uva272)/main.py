odd = True
while True:
    try:
        line = input()
        while '"' in line:
            if odd:
                line = line.replace('"', "``", 1)
            else:
                line = line.replace('"', "''", 1)
            odd = not odd
        print(line)
    except EOFError:
        break