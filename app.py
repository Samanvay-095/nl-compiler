import streamlit as st
import re
import io
import sys
import base64

from lexer import tokenize
from parser import parse
from generator import generate
from flowchart import generate_flowchart


# ---------- BACKGROUND FUNCTION ----------

def set_bg(img):

    with open(img, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# ---------- PAGE CONFIG ----------

st.set_page_config(layout="wide")


# ---------- STATE ----------

if "step" not in st.session_state:
    st.session_state.step = "onboarding"
    st.session_state.user_data = {}

if "program" not in st.session_state:
    st.session_state.program = ""

if "history" not in st.session_state:
    st.session_state.history = []


# =====================================================
# ================= ONBOARDING ========================
# =====================================================

if st.session_state.step == "onboarding":

    set_bg("Pic 2.png")

    st.title("LOGICLOOM")

    with st.form("form"):

        first = st.text_input("First Name")
        last = st.text_input("Last Name")
        email = st.text_input("Email")

        age = st.number_input("Age", 1, 100)

        purpose = st.selectbox(
            "Purpose",
            ["Learning Programming", "Hackathon", "Testing"]
        )

        language = st.selectbox(
            "Language",
            ["Python", "C", "C++", "Java"]
        )

        start = st.form_submit_button("Start")

        if start:

            if not first or not last or not email:
                st.warning("Fill all fields")

            elif not re.match(
                r"^[a-zA-Z0-9._%+-]+@gmail\.com$",
                email
            ):
                st.error("Use Gmail")

            else:

                st.session_state.user_data = {
                    "first": first,
                    "last": last,
                    "email": email,
                    "purpose": purpose,
                    "language": language
                }

                st.session_state.step = "compiler"
                st.rerun()


# =====================================================
# ================= COMPILER ==========================
# =====================================================

elif st.session_state.step == "compiler":

    set_bg("Pic 1.png")

    user = st.session_state.user_data
    lang = user["language"]


    # ---------- SIDEBAR ----------

    st.sidebar.title("User Info")

    st.sidebar.write(
        f"Name: {user['first']} {user['last']}"
    )

    st.sidebar.write(
        f"Email: {user['email']}"
    )

    st.sidebar.write(
        f"Purpose: {user['purpose']}"
    )

    st.sidebar.write(
        f"Language: {lang}"
    )

    if st.sidebar.button("Reset"):

        st.session_state.step = "onboarding"
        st.rerun()


    st.sidebar.subheader("History")

    for i, item in enumerate(
        st.session_state.history
    ):

        if st.sidebar.button(
            f"Program {i+1}"
        ):
            st.session_state.program = item
            st.rerun()


    # ---------- LAYOUT ----------

    left, right = st.columns([3,1])


    # ---------- LEFT ----------

    with left:

        st.title(
            f"Natural Language → {lang} Compiler"
        )

        program = st.text_area(
            "Write your program",
            value=st.session_state.program,
            placeholder="Write what you THINK, not how to CODE it.",
            height=300
        )

        st.session_state.program = program

        st.divider()


    # ---------- RIGHT ----------

    with right:

        st.markdown("##")

        run_lexer = st.button(
            "Run Lexer",
            use_container_width=True
        )

        run_parser = st.button(
            "Run Parser",
            use_container_width=True
        )

        run_code = st.button(
            "Generate Code",
            use_container_width=True
        )

        run_prog = st.button(
            "Run Program",
            use_container_width=True
        )

        run_flow = st.button(
            "Generate Flowchart",
            use_container_width=True
        )

        run_tree = st.button(
            "Show Parse Tree",
            use_container_width=True
        )


    # ---------- ACTIONS ----------

    if run_lexer:

        tokens = tokenize(program)

        st.subheader("Lexer")
        st.write(tokens)


    if run_parser:

        tokens = tokenize(program)
        cmds = parse(tokens)

        st.subheader("Parser")
        st.write(cmds)


    if run_code:

        if program not in st.session_state.history:
            st.session_state.history.append(program)

        tokens = tokenize(program)
        cmds = parse(tokens)

        code = generate(cmds, lang)

        st.subheader("Code")
        st.code(code)


    if run_prog:

        tokens = tokenize(program)
        cmds = parse(tokens)

        code = generate(cmds, "Python")

        st.subheader("Output")

        try:

            buf = io.StringIO()
            sys.stdout = buf

            exec(code)

            sys.stdout = sys.__stdout__

            st.code(buf.getvalue())

        except Exception as e:
            st.error(e)


    if run_flow:

        chart = generate_flowchart(program)

        st.subheader("Flowchart")
        st.graphviz_chart(chart)


    if run_tree:

        tokens = tokenize(program)
        cmds = parse(tokens)

        tree = "digraph T {\n"
        tree += "Program;\n"

        i = 0

        for c in cmds:

            n = f"n{i}"
            tree += f'{n} [label="{c[0]}"];\n'
            tree += f'Program -> {n};\n'

            for p in c[1:]:
                ch = f"{n}_{p}"
                tree += f'{ch} [label="{p}"];\n'
                tree += f'{n} -> {ch};\n'

            i += 1

        tree += "}"

        st.subheader("Parse Tree")
        st.graphviz_chart(tree)
