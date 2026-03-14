import streamlit as st
import re
import io
import sys

from lexer import tokenize
from parser import parse
from generator import generate
from flowchart import generate_flowchart


if "program" not in st.session_state:
    st.session_state.program = """create variable x equal to 5
create variable y equal to 10
print sum of x and y
repeat 2 times
print x
end"""


st.title("Natural Language Compiler")

program = st.text_area(
    "Write your program",
    st.session_state.program,
    height=250
)

st.session_state.program = program


# ---------- LEXER ----------

if st.button("Run Lexer"):

    tokens = tokenize(program)

    st.subheader("Lexer Output")
    st.write(tokens)


# ---------- PARSER ----------

if st.button("Run Parser"):

    tokens = tokenize(program)
    commands = parse(tokens)

    st.subheader("Parser Output")
    st.write(commands)


# ---------- GENERATE CODE ----------

language = st.selectbox(
    "Select Language",
    ["Python", "Java", "C++"]
)

if st.button("Generate Code"):

    tokens = tokenize(program)
    commands = parse(tokens)

    code = generate(commands, language)

    st.subheader("Generated Code")
    st.code(code)


# ---------- RUN PROGRAM ----------

if st.button("Run Program"):

    tokens = tokenize(program)
    commands = parse(tokens)

    code = generate(commands, "Python")

    st.subheader("Program Output")

    try:

        buffer = io.StringIO()
        sys.stdout = buffer

        exec(code)

        sys.stdout = sys.__stdout__

        output = buffer.getvalue()

        st.code(output)

    except Exception as e:
        st.error(e)


# ---------- FLOWCHART ----------

if st.button("Generate Flowchart"):

    chart = generate_flowchart(program)

    st.subheader("Program Flowchart")
    st.graphviz_chart(chart)