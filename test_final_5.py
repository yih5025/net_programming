import asyncio
import random

host = 'localhost'
port = 9999

message_queues = {}  # 소켓별 메시지 큐 딕셔너리

def generate_random_number():
    return random.randint(0, 40)

def generate_random_number2():
    return random.randint(0, 100)

async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)
        if data:
            received = data.decode()
            if received == '1':
                number = generate_random_number()
                message_queues[writer].append(str(number).encode())
                if writer not in writer._conn_lost:
                    writer.resume_reading()
            elif received == '2':
                number = generate_random_number2()
                message_queues[writer].append(str(number).encode())
                if writer not in writer._conn_lost:
                    writer.resume_reading()
        else:
            writer.close()
            await writer.wait_closed()
            del message_queues[writer]
            break

async def main():
    server = await asyncio.start_server(
        handle_client, host, port)

    async with server:
        await server.serve_forever()

asyncio.run(main())
