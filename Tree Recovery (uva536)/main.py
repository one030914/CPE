def find_path(preO, inO):
    if len(preO) == 0:
        return ""
    root = preO[0]
    root_index = inO.index(root)
    left_subtree = find_path(preO[1:root_index + 1], inO[:root_index])
    right_subtree = find_path(preO[root_index + 1:], inO[root_index + 1:])
    return left_subtree + right_subtree + root

while True:
    try:
        preO, inO = input().split()
        preO = list(preO)
        inO = list(inO)
        result = find_path(preO, inO)
        print(result)
    except EOFError:
        break