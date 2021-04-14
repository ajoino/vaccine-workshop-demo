"""
Asynchronous consumer with Websockets!
"""

import asyncio

from arrowhead_client.client.implementations import AsyncClient

consumer = AsyncClient.create(
        system_name='vaccine-consumer',
        address='127.0.0.1',
        port=7001,
        keyfile='../certificates/crypto/consumer.key',
        certfile='../certificates/crypto/consumer.pub',
        cafile='certificates/crypto/sysop.ca',
)

async def main(consumer: AsyncClient):
    async with consumer:
        await consumer.add_orchestration_rule('all_caps', 'GET')
        await consumer.add_orchestration_rule('echo_all', '*')

        caps = await consumer.consume_service('all_caps', json={'sentence': "We're going async now!"})

        print(caps)

        connection = await consumer.connect('echo_all')

        async with connection:
            for _ in range(5):
                data = input()
                await connection.send(data)
                print(await connection.receive())
            await connection.close()

if __name__ == '__main__':
    asyncio.run(main(consumer))
