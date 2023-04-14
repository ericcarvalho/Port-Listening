import socket

HOST = input("Entre com o ip da sua máquina: ")
PORT = int(input("Qual a porta para escuta? "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor escutando na porta {PORT}...")

    conn, addr = s.accept()
    with conn:
        print('Conexão estabelecida por', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
