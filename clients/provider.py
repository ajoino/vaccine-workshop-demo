"""
Provider
"""

from arrowhead_client.client.implementations import SyncClient

provider = SyncClient.create(
        system_name='provider',
        address='127.0.0.1',
        port=7000,
        keyfile='../certificates/crypto/provider.key',
        certfile='../certificates/crypto/provider.crt',
        cafile='../certificates/crypto/sysop.ca',
)

@provider.provided_service(
        service_definition='echo',
        service_uri='hello',  # https://127.0.0.1:7000/hello
        protocol='HTTP',
        method='GET',
        payload_format='TEXT',
        access_policy='CERTIFICATE', )
def echo(request):
    return "Got it!"

@provider.provided_service(
        service_definition='all_caps',
        service_uri='all_caps',
        protocol='HTTP',
        method='POST',
        payload_format='JSON',
        access_policy='TOKEN', )
def all_caps(request):
    req = request.read_json()
    sentence = req['sentence']
    ret = [word.upper() for word in sentence.split()]
    return {'CAPS': ret}

if __name__ == '__main__':
    provider.run_forever()