import asyncio

port = 2500
BUFSIZE = 1024

async def main():
    reader, writer = await asyncio.open_connection('localhost', port)
    