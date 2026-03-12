def generate_flowchart(program):

    lines = program.split("\n")

    chart = "digraph G {\n"
    chart += "node [shape=box];\n"

    for i,line in enumerate(lines):

        line = line.strip()

        chart += f'n{i} [label="{line}"];\n'

        if i > 0:
            chart += f'n{i-1} -> n{i};\n'

    chart += "}"

    return chart