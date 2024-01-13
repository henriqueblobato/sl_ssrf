import streamlit as st
import subprocess


def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"


def main():
    st.title("Command Executor")

    # Input box for user to enter a command
    command_input = st.text_input("$ ")

    # Button to execute the command
    if st.button("Execute"):
        if command_input:
            st.text("Executing command...")
            result = execute_command(command_input)
            st.text("Command result:")
            st.text(result)


if __name__ == "__main__":
    main()
