odd = True
while True:
    try:
        line = input()
        while '"' in line:
            line = line.replace('"', "``", 1) if odd else line.replace('"', "''", 1)
            odd = not odd
        print(line)
    except EOFError:
        break