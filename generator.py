def generate(commands, language):

    code = []
    indent = 0

# ---------- PYTHON ----------
    if language == "Python":

        for cmd in commands:

            if cmd[0] == "declare":
                code.append("    "*indent + f"{cmd[1]} = {cmd[2]}")

            elif cmd[0] == "print":
                code.append("    "*indent + f"print({cmd[1]})")

            elif cmd[0] == "sum":
                code.append("    "*indent + f"print({cmd[1]} + {cmd[2]})")

            elif cmd[0] == "loop":
                code.append("    "*indent + f"for _ in range({cmd[1]}):")
                indent += 1

            elif cmd[0] == "end":
                indent -= 1

# ---------- C ----------
    elif language == "C":

        code.append("#include <stdio.h>")
        code.append("int main(){")
        indent = 1

        for cmd in commands:

            if cmd[0] == "declare":
                code.append("    "*indent + f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "print":
                code.append("    "*indent + f'printf("%d\\n",{cmd[1]});')

            elif cmd[0] == "sum":
                code.append("    "*indent + f'printf("%d\\n",{cmd[1]} + {cmd[2]});')

            elif cmd[0] == "loop":
                code.append("    "*indent + f"for(int i=0;i<{cmd[1]};i++){{")
                indent += 1

            elif cmd[0] == "end":
                indent -= 1
                code.append("    "*indent + "}")

        code.append("return 0;")
        code.append("}")

# ---------- C++ ----------
    elif language == "C++":

        code.append("#include <iostream>")
        code.append("using namespace std;")
        code.append("int main(){")
        indent = 1

        for cmd in commands:

            if cmd[0] == "declare":
                code.append("    "*indent + f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "print":
                code.append("    "*indent + f"cout << {cmd[1]} << endl;")

            elif cmd[0] == "sum":
                code.append("    "*indent + f"cout << {cmd[1]} + {cmd[2]} << endl;")

            elif cmd[0] == "loop":
                code.append("    "*indent + f"for(int i=0;i<{cmd[1]};i++){{")
                indent += 1

            elif cmd[0] == "end":
                indent -= 1
                code.append("    "*indent + "}")

        code.append("return 0;")
        code.append("}")

# ---------- JAVA ----------
    elif language == "Java":

        code.append("public class Main {")
        code.append("public static void main(String[] args) {")
        indent = 1

        for cmd in commands:

            if cmd[0] == "declare":
                code.append("    "*indent + f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "print":
                code.append("    "*indent + f"System.out.println({cmd[1]});")

            elif cmd[0] == "sum":
                code.append("    "*indent + f"System.out.println({cmd[1]} + {cmd[2]});")

            elif cmd[0] == "loop":
                code.append("    "*indent + f"for(int i=0;i<{cmd[1]};i++){{")
                indent += 1

            elif cmd[0] == "end":
                indent -= 1
                code.append("    "*indent + "}")

        code.append("}")
        code.append("}")

    return "\n".join(code)