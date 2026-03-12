import re

def tokenize(program):

    tokens = []

    lines = program.lower().split("\n")

    for line in lines:

        words = re.findall(r'\w+', line)

        tokens.append(words)

    return tokens