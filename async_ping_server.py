import asyncio

async def handle_asyncclient(reader, writer):
    print('client: ', writer.get_extra_info('peerman'))

    while True:
        data = await reader.read(8)
        if data == b'ping':
            writer.write(b'pong')
            await writer.drain()
            