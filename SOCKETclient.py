import socket
import threading

def receive_messages(sock):
    buffer = ''
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                break
            buffer += data
            while '\n' in buffer:
                line, buffer = buffer.split('\n', 1)
                print(f"Received: {line.strip()}")
                reply = input("Reply> ")
                sock.send((reply + '\n').encode('utf-8'))
        except:
            break

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9999))
    receive_messages(s)
