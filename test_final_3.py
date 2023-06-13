import socket
import random
import select

host = 'localhost'
port = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

inputs = [server_socket] # 소켓 입력을 감시할 리스트
outputs = [] # 소켓 출력 대기 리스트
message_queues = {} # 소켓별 메시지 큐 딕셔너리

def generate_random_number():
    return random.randint(0, 40)

def generate_random_number2():
    return random.randint(0, 100)

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for sock in readable:
        if sock is server_socket:
            # 새로운 클라이언트가 접속한 경우
            client_socket, client_address = server_socket.accept()
            inputs.append(client_socket)
            message_queues[client_socket] = []
        else:
            # 기존 클라이언트로부터 데이터를 받은 경우
            data = sock.recv(1024)
            if data:
                # 클라이언트로부터 데이터를 정상적으로 받은 경우
                received = data.decode()
                if received == '1':
                    number = generate_random_number()
                    message_queues[sock].append(str(number).encode())
                    if sock not in outputs:
                        outputs.append(sock)
                elif received == '2':
                    number = generate_random_number2()
                    message_queues[sock].append(str(number).encode())
                    if sock not in outputs:
                        outputs.append(sock)
            else:
                # 클라이언트와의 연결이 끊어진 경우
                if sock in outputs:
                    outputs.remove(sock)
                inputs.remove(sock)
                sock.close()
                del message_queues[sock]

    for sock in writable:
        # 클라이언트에게 데이터를 전송
        if message_queues[sock]:
            data = message_queues[sock].pop(0)
            sock.send(data)
        else:
            outputs.remove(sock)

    for sock in exceptional:
        # 예외 발생 시 클라이언트와의 연결을 닫음
        inputs.remove(sock)
        if sock in outputs:
            outputs.remove(sock)
        sock.close()
        del message_queues[sock]
