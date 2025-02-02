def code(x: int, y: int) -> int:
    return 2**x*(2*y+1)-1

def decode(n: int) -> tuple[int, int]:
    n += 1
    x = 0
    while n % 2 == 0:
        n //= 2
        x += 1
    y = (n-1)//2
    return x, y



def get_variable(n: int) -> str:
    if n == 0:
        return "Y"
    if n % 2 == 1:
        return f"X{(n+1)//2}"
    else:
        return f"Z{n//2}"

def get_label(n: int) -> str | None:
    if n == 0:
        return None
    if n % 5 == 1:
        return f"A{n//5 + 1}"
    if n % 5 == 2:
        return f"B{n//5 + 1}"
    if n % 5 == 3:
        return f"C{n//5 + 1}"
    if n % 5 == 4:
        return f"D{n//5 + 1}"
    if n % 5 == 0:
        return f"E{n//5}"

def get_line_code(label: int, variable: int, intruction: int) -> int:
    return code(label, code(variable, intruction))

def get_line_code_inv(line_code: int) -> tuple[int, int, int]:
    label, instable = decode(line_code)
    intruction, variable = decode(instable)
    return label, intruction, variable

def log_snapshot(i: int, snapshot: list[int]):
    print(i, end=" ")
    for i in range(len(snapshot)):
        print(snapshot[i], end=" ")
    print()

def get_snapshot_index(variable: int, X_MAX: int, Z_MAX: int) -> int:
    if variable == 0:
        return X_MAX + Z_MAX
    if variable % 2 == 1:
        return (variable+1)//2 - 1
    else:
        return X_MAX + variable//2 - 1

def get_max_X(lines: list[list[int]]) -> int:
    res = 0
    for line in lines:
        if line[2] % 2 == 1 and line[2] > res:
            res = (line[2]+1)//2
    return res

def get_max_Z(lines: list[list[int]]) -> int:
    res = 0
    for line in lines:
        if line[2] % 2 == 0 and line[2] != 0 and line[2] > res:
            res = line[2]//2
    return res

def get_line_index_from_label(label: int, lines: list[list[int]]) -> int | None:
    for index in range(len(lines)):
        if lines[index][0] == label:
            return index+1
    return None

def get_start_snapshot(lines: list[list[int]], inputs: list[int]):
    X_MAX = get_max_X(lines)
    Z_MAX = get_max_Z(lines)
    snapshot = []
    for x in range(X_MAX):
        if x < len(inputs):
            snapshot.append(inputs[x])
        else:
            snapshot.append(0)
    for z in range(Z_MAX):
        snapshot.append(0)
    snapshot.append(0) # for Y
    return snapshot