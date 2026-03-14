def parse(tokens):

    commands = []

    for line in tokens:

        if not line:
            continue

        if line[0] == "create":
            commands.append(("declare", line[2], line[-1]))

        elif line[0] == "set":
            commands.append(("set", line[1], line[-1]))

        elif line[0] == "print" and "sum" in line:
            commands.append(("sum", line[-3], line[-1]))

        elif line[0] == "print" and "division" in line:
            commands.append(("division", line[-3], line[-1]))

        elif line[0] == "print":
            commands.append(("print", line[1]))

        elif line[0] == "repeat":
            commands.append(("loop", line[1]))

        elif line[0] == "while":
            commands.append(("while", line[1], line[2], line[3]))

        elif line[0] == "do":
            commands.append(("do",))

        elif line[0] == "if":

            if "less" in line:
                commands.append(("if", line[1], "<", line[-1]))

            elif "greater" in line:
                commands.append(("if", line[1], ">", line[-1]))

            elif "equal" in line:
                commands.append(("if", line[1], "==", line[-1]))

        elif line[0] == "elif":

            if "less" in line:
                commands.append(("elif", line[1], "<", line[-1]))

            elif "greater" in line:
                commands.append(("elif", line[1], ">", line[-1]))

            elif "equal" in line:
                commands.append(("elif", line[1], "==", line[-1]))

        elif line[0] == "else":
            commands.append(("else",))

        elif line[0] == "end":
            commands.append(("end",))

    return commands