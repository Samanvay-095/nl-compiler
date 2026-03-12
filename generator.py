def generate(commands, language):

    code = []
    indent = 0

# -------- PYTHON --------

    if language == "Python":

        for cmd in commands:

            if cmd[0] == "declare":
                code.append("    "*indent + f"{cmd[1]} = {cmd[2]}")

            elif cmd[0] == "print":
                code.append("    "*indent + f"print({cmd[1]})")

            elif cmd[0] == "sum":
                code.append("    "*indent + f"print({cmd[1]} + {cmd[2]})")

            elif cmd[0] == "loop":
                code.append("    "*indent + f"for i in range({cmd[1]}):")
                indent += 1

            elif cmd[0] == "end":
                indent -= 1

# -------- C --------

    elif language == "C":

        code.append("#include <stdio.h>")
        code.append("int main(){")

        for cmd in commands:

            if cmd[0] == "declare":
                code.append(f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "print":
                code.append(f'printf("%d\\n",{cmd[1]});')

        code.append("return 0;")
        code.append("}")

# -------- C++ --------

    elif language == "C++":

        code.append("#include <iostream>")
        code.append("using namespace std;")
        code.append("int main(){")

        for cmd in commands:

            if cmd[0] == "declare":
                code.append(f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "print":
                code.append(f"cout << {cmd[1]} << endl;")

        code.append("return 0;")
        code.append("}")

# -------- JAVA --------

    elif language == "Java":

        code.append("public class Main {")
        code.append("public static void main(String[] args) {")

        for cmd in commands:

            if cmd[0] == "declare":
                code.append(f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "print":
                code.append(f"System.out.println({cmd[1]});")

        code.append("}")
        code.append("}")

    return "\n".join(code)