"""
Consumer
"""

from arrowhead_client.client.implementations import SyncClient

consumer = SyncClient.create(
        system_name='consumer',
        address='127.0.0.1',
        port=7001,
        keyfile='../certificates/crypto/consumer.key',
        certfile='../certificates/crypto/consumer.crt',
        cafile='../certificates/crypto/sysop.ca',
)

if __name__ == '__main__':
    consumer.setup()

    #consumer.add_orchestration_rule('echo', 'GET')
    #response = consumer.consume_service('echo')
    #print(response.read_json())

    consumer.add_orchestration_rule('all_caps', 'POST')
    sentence = "This consumer is an example for the Vaccine workshop!"
    response = consumer.consume_service('all_caps', json={'sentence': sentence})
    print(response.read_json()['CAPS'])