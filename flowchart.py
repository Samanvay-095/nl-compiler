def generate_flowchart(program):

    lines = program.split("\n")

    chart = "digraph G {\n"
    chart += "node [shape=oval];\n"

    chart += 'start [label="start"];\n'

    prev = "start"
    node_id = 0
    last_line = ""

    for line in lines:

        line = line.strip()

        if line == "":
            continue

        last_line = line.lower()

        name = f"node{node_id}"

        chart += f'{name} [label="{line}"];\n'
        chart += f"{prev} -> {name};\n"

        prev = name
        node_id += 1

    # ✅ add end only if not already end
    if last_line != "end":
        chart += 'end [label="end"];\n'
        chart += f"{prev} -> end;\n"

    chart += "}"

    return chart
