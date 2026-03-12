from lexer import tokenize
from parser import parse
from generator import generate

def compile_program(program, language):

    tokens = tokenize(program)
    commands = parse(tokens)
    code = generate(commands, language)

    return tokens, commands, code