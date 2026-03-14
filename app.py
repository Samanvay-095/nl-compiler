import streamlit as st
import re
import io
import sys

from lexer import tokenize
from parser import parse
from generator import generate
from flowchart import generate_flowchart

# ---------- SESSION STATE ----------

if "step" not in st.session_state:
    st.session_state.step = "onboarding"
    st.session_state.user_data = {}

if "program" not in st.session_state:
    st.session_state.program = """Write what you THINK,not how to CODE it."""

if "history" not in st.session_state:
    st.session_state.history = []

# ---------- ONBOARDING ----------

if st.session_state.step == "onboarding":

    st.title("LOGICLOOM")

    with st.form("user_form"):

        first = st.text_input("First Name")
        last = st.text_input("Last Name")
        email = st.text_input("Email")

        age = st.number_input("Age", 1, 100)

        purpose = st.selectbox(
            "Purpose",
            ["Learning Programming", "Hackathon Demo", "Testing"]
        )

        language = st.selectbox(
            "Select Output Language",
            ["Python", "C", "C++", "Java"]
        )

        start = st.form_submit_button("Start Compiler")

        if start:

            if not first or not last or not email:
                st.warning("Please fill all fields")

            elif not re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email):
                st.error("Wrong Email! Enter valid Gmail")

            else:

                st.session_state.user_data = {
                    "first": first,
                    "last": last,
                    "email": email,
                    "age": age,
                    "purpose": purpose,
                    "language": language
                }

                st.session_state.step = "compiler"
                st.rerun()

# ---------- COMPILER PAGE ----------

elif st.session_state.step == "compiler":

    user = st.session_state.user_data
    language = user["language"]

    st.sidebar.title("User Info")
    st.sidebar.write(f"Name: {user['first']} {user['last']}")
    st.sidebar.write(f"Email: {user['email']}")
    st.sidebar.write(f"Purpose: {user['purpose']}")
    st.sidebar.write(f"Language: {language}")

    if st.sidebar.button("Reset"):
        st.session_state.step = "onboarding"
        st.rerun()

# ---------- HISTORY ----------

    st.sidebar.subheader("History")

    for i, item in enumerate(st.session_state.history):

        if st.sidebar.button(f"Program {i+1}"):

            st.session_state.program = item
            st.rerun()

# ---------- TITLE BAR WITH BUTTONS ----------

    col1, col2, col3, col4, col5, col6 = st.columns([5,1,1,1,1,1])

    with col1:
        st.title(f"Natural Language → {language} Compiler")

    with col2:
        run_lexer = st.button("Lexer")

    with col3:
        run_parser = st.button("Parser")

    with col4:
        run_generate = st.button("Generate")

    with col5:
        run_execute = st.button("Run")

    with col6:
        run_flow = st.button("Flow")

# ---------- PROGRAM INPUT ----------

    program = st.text_area(
        "Write your program",
        st.session_state.program,
        height=70
    )

    st.session_state.program = program

    st.divider()

# ---------- LEXER ----------

    if run_lexer:

        tokens = tokenize(program)

        st.subheader("Lexer Output")
        st.write(tokens)

# ---------- PARSER ----------

    if run_parser:

        tokens = tokenize(program)
        commands = parse(tokens)

        st.subheader("Parser Output")
        st.write(commands)

# ---------- GENERATE CODE ----------

    if run_generate:

        if program not in st.session_state.history:
            st.session_state.history.append(program)

        tokens = tokenize(program)
        commands = parse(tokens)

        code = generate(commands, language)

        st.subheader("Generated Code")
        st.code(code)

# ---------- RUN PROGRAM ----------

    if run_execute:

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

    if run_flow:

        chart = generate_flowchart(program)

        st.subheader("Program Flowchart")
        st.graphviz_chart(chart)