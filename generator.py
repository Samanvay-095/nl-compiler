def generate(commands, language):

    # ------------------ PYTHON ------------------
    if language == "Python":
        code = []
        indent = 0

        for cmd in commands:

            if cmd[0] == "declare":
                code.append("    "*indent + f"{cmd[1]} = {cmd[2]}")

            elif cmd[0] == "set":
                code.append("    "*indent + f"{cmd[1]} = {cmd[2]}")

            elif cmd[0] == "print":
                code.append("    "*indent + f"print({cmd[1]})")

            elif cmd[0] == "sum":
                code.append("    "*indent + f"print({cmd[1]} + {cmd[2]})")

            elif cmd[0] == "division":
                code.append("    "*indent + f"print({cmd[1]} / {cmd[2]})")

            elif cmd[0] == "loop":
                code.append("    "*indent + f"for i in range({cmd[1]}):")
                indent += 1

            elif cmd[0] == "while":
                code.append("    "*indent + f"while {cmd[1]} {cmd[2]} {cmd[3]}:")
                indent += 1

            elif cmd[0] == "do":
                code.append("    "*indent + "while True:")
                indent += 1

            elif cmd[0] == "if":
                code.append("    "*indent + f"if {cmd[1]} {cmd[2]} {cmd[3]}:")
                indent += 1

            elif cmd[0] == "elif":
                indent -= 1
                code.append("    "*indent + f"elif {cmd[1]} {cmd[2]} {cmd[3]}:")
                indent += 1

            elif cmd[0] == "else":
                indent -= 1
                code.append("    "*indent + "else:")
                indent += 1

            elif cmd[0] == "end":
                indent -= 1

        return "\n".join(code)

    # ------------------ JAVA ------------------
    if language == "Java":
        code = [
            "public class Program {",
            "public static void main(String[] args){"
        ]
        indent = 1

        for cmd in commands:

            pad = "    " * indent

            if cmd[0] == "declare" or cmd[0] == "set":
                code.append(pad + f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "print":
                code.append(pad + f"System.out.println({cmd[1]});")

            elif cmd[0] == "sum":
                code.append(pad + f"System.out.println({cmd[1]} + {cmd[2]});")

            elif cmd[0] == "division":
                code.append(pad + f"System.out.println({cmd[1]} / {cmd[2]});")

            elif cmd[0] == "loop":
                code.append(pad + f"for(int i=0; i<{cmd[1]}; i++)"+"{")
                indent += 1

            elif cmd[0] == "while":
                code.append(pad + f"while({cmd[1]} {cmd[2]} {cmd[3]})"+"{")
                indent += 1

            elif cmd[0] == "do":
                code.append(pad + "do {")
                indent += 1

            elif cmd[0] == "if":
                code.append(pad + f"if({cmd[1]} {cmd[2]} {cmd[3]})"+"{")
                indent += 1

            elif cmd[0] == "elif":
                indent -= 1
                code.append(pad + f"else if({cmd[1]} {cmd[2]} {cmd[3]})"+"{")
                indent += 1

            elif cmd[0] == "else":
                indent -= 1
                code.append(pad + "else {")
                indent += 1

            elif cmd[0] == "end":
                indent -= 1
                code.append("    "*indent + "}")

        code.append("    }")
        code.append("}")
        return "\n".join(code)

    # ------------------ C++ ------------------
    if language == "C++":
        code = [
            "#include <iostream>",
            "using namespace std;",
            "int main(){"
        ]
        indent = 1

        for cmd in commands:

            pad = "    " * indent

            if cmd[0] == "declare" or cmd[0] == "set":
                code.append(pad + f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "print":
                code.append(pad + f"cout << {cmd[1]} << endl;")

            elif cmd[0] == "sum":
                code.append(pad + f"cout << {cmd[1]} + {cmd[2]} << endl;")

            elif cmd[0] == "division":
                code.append(pad + f"cout << {cmd[1]} / {cmd[2]} << endl;")

            elif cmd[0] == "loop":
                code.append(pad + f"for(int i=0; i<{cmd[1]}; i++)"+"{")
                indent += 1

            elif cmd[0] == "while":
                code.append(pad + f"while({cmd[1]} {cmd[2]} {cmd[3]})"+"{")
                indent += 1

            elif cmd[0] == "do":
                code.append(pad + "do {")
                indent += 1

            elif cmd[0] == "if":
                code.append(pad + f"if({cmd[1]} {cmd[2]} {cmd[3]})"+"{")
                indent += 1

            elif cmd[0] == "elif":
                indent -= 1
                code.append(pad + f"else if({cmd[1]} {cmd[2]} {cmd[3]})"+"{")
                indent += 1

            elif cmd[0] == "else":
                indent -= 1
                code.append(pad + "else {")
                indent += 1

            elif cmd[0] == "end":
                indent -= 1
                code.append("    "*indent + "}")

        code.append("    return 0;")
        code.append("}")
        return "\n".join(code)

    # ------------------ C ------------------
    if language == "C":
        code = [
            "#include <stdio.h>",
            "int main(){"
        ]
        indent = 1

        for cmd in commands:

            pad = "    " * indent

            if cmd[0] == "declare" or cmd[0] == "set":
                code.append(pad + f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "print":
                code.append(pad + f"printf(\"%d\\n\", {cmd[1]});")

            elif cmd[0] == "sum":
                code.append(pad + f"printf(\"%d\\n\", {cmd[1]} + {cmd[2]});")

            elif cmd[0] == "division":
                code.append(pad + f"printf(\"%d\\n\", {cmd[1]} / {cmd[2]});")

            elif cmd[0] == "loop":
                code.append(pad + f"for(int i=0; i<{cmd[1]}; i++)"+"{")
                indent += 1

            elif cmd[0] == "while":
                code.append(pad + f"while({cmd[1]} {cmd[2]} {cmd[3]})"+"{")
                indent += 1

            elif cmd[0] == "do":
                code.append(pad + "do {")
                indent += 1

            elif cmd[0] == "if":
                code.append(pad + f"if({cmd[1]} {cmd[2]} {cmd[3]})"+"{")
                indent += 1

            elif cmd[0] == "elif":
                indent -= 1
                code.append(pad + f"else if({cmd[1]} {cmd[2]} {cmd[3]})"+"{")
                indent += 1

            elif cmd[0] == "else":
                indent -= 1
                code.append(pad + "else {")
                indent += 1

            elif cmd[0] == "end":
                indent -= 1
                code.append("    "*indent + "}")

        code.append("    return 0;")
        code.append("}")
        return "\n".join(code)

    return "// Language not implemented"