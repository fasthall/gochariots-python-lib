import grpc
import batcherrpc_pb2
import batcherrpc_pb2_grpc
from fnvhash import fnv1a_64

class RPCClient:
    def __init__(self, host):
        channel = grpc.insecure_channel(host)
        self.stub = batcherrpc_pb2_grpc.BatcherRPCStub(channel)
    
    def postRecord(self, record):
        rpcRecord = batcherrpc_pb2.RPCRecord(
            id = record.id,
            host = record.host,
            tags = record.tags,
            parent = record.parent,
            seed = record.seed
        )
        return self.stub.ReceiveRecord(rpcRecord)

    def asyncPostRecord(self, record):
        rpcRecord = batcherrpc_pb2.RPCRecord(
            id = record.id,
            host = record.host,
            tags = record.tags,
            parent = record.parent,
            seed = record.seed
        )
        return self.stub.ReceiveRecord.future(rpcRecord)

class Record:
    """Record consists of key-value pairs and casual dependency"""
    def __init__(self, id, host, seed):
        self.id = id
        self.host = host
        self.seed = seed
        self.parent = ""
        self.tags = {}

    def setParent(self, parent):
        self.parent = parent

    def addTag(self, key, value):
        self.tags[key] = value