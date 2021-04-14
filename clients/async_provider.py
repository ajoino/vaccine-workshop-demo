"""
Asynchronous provider with WebSockets!
"""

from fastapi import WebSocket
from pydantic import BaseModel

from arrowhead_client.client.implementations import AsyncClient

provider = AsyncClient.create(
        system_name='vaccine-provider',
        address='127.0.0.1',
        port=7000,
        keyfile='../certificates/crypto/provider.key',
        certfile='../certificates/crypto/provider.pub',
        cafile='certificates/crypto/sysop.ca',
)

class SentenceModel(BaseModel):
    sentence: str

@provider.provided_service(
        service_definition='all_caps',
        service_uri='all_caps',
        protocol='HTTP',
        method='POST',
        payload_format='JSON',
        access_policy='CERTIFICATE', )
async def all_caps(request: SentenceModel):
    ret = [word.upper() for word in request.sentence.split()]
    return ret

@provider.provided_service(
        service_definition='echo_all',
        service_uri='echo_all',
        protocol='WS',
        method='',
        payload_format='TEXT',
        access_policy='CERTIFICATE' )
async def echo_all(websocket: WebSocket):
    await websocket.accept()
    all_data = []
    while True:
        data = await websocket.receive_text()
        all_data.append(data)
        await websocket.send_text('\n'.join(all_data))
