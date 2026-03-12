def generate(commands, language):

    if language == "Python":

        code = []
        indent = 0

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

        return "\n".join(code)

    if language == "Java":

        code = [
            "public class Program {",
            "public static void main(String[] args){"
        ]

        for cmd in commands:

            if cmd[0] == "declare":
                code.append(f"int {cmd[1]} = {cmd[2]};")

            elif cmd[0] == "sum":
                code.append(f'System.out.println({cmd[1]} + {cmd[2]});')

            elif cmd[0] == "print":
                code.append(f'System.out.println({cmd[1]});')

            elif cmd[0] == "loop":
                code.append(f"for(int i=0;i<{cmd[1]};i++)"+"{")

            elif cmd[0] == "end":
                code.append("}")

        code.append("}")
        code.append("}")

        return "\n".join(code)

    return "// Language generation not implemented yet"