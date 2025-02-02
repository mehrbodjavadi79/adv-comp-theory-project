from utils import get_line_code_inv, get_line_index_from_label, get_max_X, get_max_Z, get_snapshot_index, get_start_snapshot, get_variable, log_snapshot


code_lines = list(map(int, input().split()))
inputs = list(map(int, input().split()))
lines = []

for code_line in code_lines:
    label, instruction, variable = get_line_code_inv(int(code_line))
    lines.append([label, instruction, variable])



X_MAX = get_max_X(lines)
Z_MAX = get_max_Z(lines)
snapshot = get_start_snapshot(lines, inputs)
i=1 # the current line index which is going to be executed


while True:
    if i > len(lines):
        break
    log_snapshot(i, snapshot)
    _, instruction, variable = lines[i-1]
    if instruction == 0:
        i += 1
    if instruction == 1:
        i += 1
        index = get_snapshot_index(variable, X_MAX, Z_MAX)
        snapshot[index] = snapshot[index] + 1
    if instruction == 2:
        i += 1
        index = get_snapshot_index(variable, X_MAX, Z_MAX)
        if snapshot[index] != 0:
            snapshot[index] = snapshot[index] - 1
    if instruction >= 3:
        index = get_snapshot_index(variable, X_MAX, Z_MAX)
        if snapshot[index] != 0:
            next_i = get_line_index_from_label(instruction-2, lines)
            if next_i != None:
                i = next_i
            else:
                break
        else:
            i += 1
