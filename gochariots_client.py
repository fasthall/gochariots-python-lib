import grpc
import batcherrpc_pb2
import batcherrpc_pb2_grpc
from fnvhash import fnv1a_64

class RPCClient:
    def __init__(self, host):
        channel = grpc.insecure_channel(host)
        self.stub = batcherrpc_pb2_grpc.BatcherRPCStub(channel)
    
    def post(self, record):
        rpcRecord = batcherrpc_pb2.RPCRecord()
        for k in record.tags:
            rpcRecord.tags[k] = record.tags[k]
        rpcRecord.seed = record.seed
        for h in record.hash:
            rpcRecord.hash.append(h)
        return self.stub.ReceiveRecord(rpcRecord)

class Record:
    """Record consists of key-value pairs and casual dependency"""
    def __init__(self, seed):
        self.tags = {}
        self.seed = seed
        self.hash = []

    def addHash(self, hash):
        self.hash.append(hash)

    def add(self, key, value):
        self.tags[key] = value

def getHash(key, value):
    return fnv1a_64((key + ":" + value).encode())
