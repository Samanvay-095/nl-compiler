import streamlit as st
import speech_recognition as sr
import re
from lexer import tokenize
from parser import parse
from generator import generate
from flowchart import generate_flowchart
import io
import sys


# ---------- VOICE FUNCTION ----------

def listen_voice():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = r.listen(source)

        text = r.recognize_google(audio)
        return text

    except:
        return "Could not understand"


# ---------- SESSION STATE ----------

if "step" not in st.session_state:
    st.session_state.step = "onboarding"
    st.session_state.user_data = {}


# ---------- ONBOARDING PAGE ----------

if st.session_state.step == "onboarding":

    st.title("Natural Language Compiler")

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

    # voice button outside form
    if st.button("🎤 Speak"):
        voice_text = listen_voice()
        st.write("You said:", voice_text)

    if start:

        if not first or not last or not email:
            st.warning("Please fill all fields")

        elif not re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email):
            st.error("Wrong Email! Please enter Gmail")

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
    st.sidebar.write(f"Age: {user['age']}")
    st.sidebar.write(f"Language: {language}")

    if st.sidebar.button("Reset"):
        st.session_state.step = "onboarding"
        st.rerun()

    st.title(f"Natural Language → {language} Compiler")

    example = """create variable x equal to 5
create variable y equal to 10
print sum of x and y
repeat 2 times
print x
end"""

    program = st.text_area(
        "Write your program",
        example,
        height=250
    )


# ---------- VOICE INPUT ----------

    if st.button("🎤 Voice Input"):

        text = listen_voice()

        program += "\n" + text

        st.success("Voice added")


    st.divider()


# ---------- LEXER ----------

    if st.button("Run Lexer"):

        tokens = tokenize(program)

        st.subheader("Tokens")
        st.write(tokens)


# ---------- PARSER ----------

    if st.button("Run Parser"):

        tokens = tokenize(program)
        commands = parse(tokens)

        st.subheader("Commands")
        st.write(commands)


# ---------- CODE ----------

    if st.button("Generate Code"):

        tokens = tokenize(program)
        commands = parse(tokens)

        code = generate(commands, language)

        st.subheader("Generated Code")
        st.code(code)


# ---------- RUN ----------

    if st.button("Run Program"):

        tokens = tokenize(program)
        commands = parse(tokens)

        code = generate(commands, "Python")

        st.subheader("Output")

        try:

            buffer = io.StringIO()
            sys.stdout = buffer

            exec(code)

            sys.stdout = sys.__stdout__

            st.code(buffer.getvalue())

        except Exception as e:
            st.error(e)


# ---------- FLOWCHART ----------

    if st.button("Flowchart"):

        chart = generate_flowchart(program)

        st.graphviz_chart(chart)