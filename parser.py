def parse(tokens):

    commands = []

    for line in tokens:

        if not line:
            continue

        if line[0] == "create":
            commands.append(("declare", line[2], line[-1]))

        elif line[0] == "print" and "sum" in line:
            commands.append(("sum", line[-3], line[-1]))

        elif line[0] == "print":
            commands.append(("print", line[1]))

        elif line[0] == "repeat":
            commands.append(("loop", line[1]))

        elif line[0] == "end":
            commands.append(("end",))

    return commands