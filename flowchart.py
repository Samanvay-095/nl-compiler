def generate_flowchart(program):

    lines = program.split("\n")

    chart = "digraph G {\n"
 
    for i in range(len(lines)):

        chart += f'node{i} [label="{lines[i]}"];\n'

        if i > 0:
            chart += f"node{i-1} -> node{i};\n"

    chart += "}"

    return chart