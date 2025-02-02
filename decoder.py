from utils import get_label, get_line_code_inv, get_variable

code_lines = list(map(int, input().split()))

for code_line in code_lines:
    label, instruction, variable = get_line_code_inv(code_line)
    line = ""
    if label != 0:
        line += f"[{get_label(label)}] "
    if instruction == 0:
        v = get_variable(variable)
        line += f"{v} <- {v}"
    if instruction == 1:
        v = get_variable(variable)
        line += f"{v} <- {v} + 1"
    if instruction == 2:
        v = get_variable(variable)
        line += f"{v} <- {v} - 1"
    if instruction >= 3:
        v = get_variable(variable)
        tagretLabel: int = instruction-2
        line += f"IF {v} != 0 GOTO {get_label(tagretLabel)}"
    print(line, "h9")
