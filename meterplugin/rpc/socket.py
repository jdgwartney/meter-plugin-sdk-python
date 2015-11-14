import json
from tinyrpc.client import RPCClient
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol


from tinyrpc.transports import ClientTransport


class SocketClientTransport(ClientTransport):

    def __init__(self, host='localhost', port=23):
        self._host = host
        self._port = port

    def send_message(self, message, expect_reply=True):
        print(message)
        m = json.loads(message)
        response = {"jsonrpc": "2.0", "id": m['id'], "result": {"status": "Ok"}}
        r = json.dumps(response)
        return r




