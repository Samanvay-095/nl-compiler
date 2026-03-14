def generate(commands, language):

# ---------------- PYTHON ----------------

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

            elif cmd[0] == "difference":
                code.append("    "*indent + f"print({cmd[1]} - {cmd[2]})")

            elif cmd[0] == "subtraction":
                code.append("    "*indent + f"print({cmd[1]} - {cmd[2]})")

            elif cmd[0] == "division":
                code.append("    "*indent + f"print({cmd[1]} / {cmd[2]})")

            elif cmd[0] == "loop":
                code.append("    "*indent + f"for i in range({cmd[1]}):")
                indent += 1

            elif cmd[0] == "while":
                code.append("    "*indent + f"while {cmd[1]} {cmd[2]} {cmd[3]}:")
                indent += 1

            elif cmd[0] == "if":
                code.append("    "*indent + f"if {cmd[1]} {cmd[2]} {cmd[3]}:")
                indent += 1

            elif cmd[0] == "else":
                indent -= 1
                code.append("    "*indent + "else:")
                indent += 1

            elif cmd[0] == "end":
                indent -= 1

        return "\n".join(code)


# ---------------- JAVA ----------------

    if language == "Java":

        code = [
            "public class Program {",
            "public static void main(String[] args){"
        ]

        indent = "    "

        for cmd in commands:

            if cmd[0] == "declare":
                code.append(indent + f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "set":
                code.append(indent + f"{cmd[1]} = {cmd[2]};")

            elif cmd[0] == "print":
                code.append(indent + f"System.out.println({cmd[1]});")

            elif cmd[0] == "sum":
                code.append(indent + f"System.out.println({cmd[1]} + {cmd[2]});")

            elif cmd[0] == "difference" or cmd[0] == "subtraction":
                code.append(indent + f"System.out.println({cmd[1]} - {cmd[2]});")

            elif cmd[0] == "division":
                code.append(indent + f"System.out.println({cmd[1]} / {cmd[2]});")

            elif cmd[0] == "loop":
                code.append(indent + f"for(int i=0;i<{cmd[1]};i++)"+"{")

            elif cmd[0] == "while":
                code.append(indent + f"while({cmd[1]} {cmd[2]} {cmd[3]})"+"{")

            elif cmd[0] == "if":
                code.append(indent + f"if({cmd[1]} {cmd[2]} {cmd[3]})"+"{")

            elif cmd[0] == "else":
                code.append(indent + "} else {")

            elif cmd[0] == "end":
                code.append(indent + "}")

        code.append("}")
        code.append("}")

        return "\n".join(code)


# ---------------- C++ ----------------

    if language == "C++":

        code = [
            "#include <iostream>",
            "using namespace std;",
            "int main(){"
        ]

        indent = "    "

        for cmd in commands:

            if cmd[0] == "declare":
                code.append(indent + f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "set":
                code.append(indent + f"{cmd[1]} = {cmd[2]};")

            elif cmd[0] == "print":
                code.append(indent + f"cout << {cmd[1]} << endl;")

            elif cmd[0] == "sum":
                code.append(indent + f"cout << {cmd[1]} + {cmd[2]} << endl;")

            elif cmd[0] == "difference" or cmd[0] == "subtraction":
                code.append(indent + f"cout << {cmd[1]} - {cmd[2]} << endl;")

            elif cmd[0] == "division":
                code.append(indent + f"cout << {cmd[1]} / {cmd[2]} << endl;")

            elif cmd[0] == "loop":
                code.append(indent + f"for(int i=0;i<{cmd[1]};i++)"+"{")

            elif cmd[0] == "while":
                code.append(indent + f"while({cmd[1]} {cmd[2]} {cmd[3]})"+"{")

            elif cmd[0] == "if":
                code.append(indent + f"if({cmd[1]} {cmd[2]} {cmd[3]})"+"{")

            elif cmd[0] == "else":
                code.append(indent + "} else {")

            elif cmd[0] == "end":
                code.append(indent + "}")

        code.append(indent + "return 0;")
        code.append("}")

        return "\n".join(code)


# ---------------- DEFAULT ----------------

    return "// Language not implemented"