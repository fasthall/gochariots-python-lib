import grpc
import batcherrpc_pb2
import batcherrpc_pb2_grpc

class RPCClient:
    def __init__(self, host):
        channel = grpc.insecure_channel(host)
        self.stub = batcherrpc_pb2_grpc.BatcherRPCStub(channel)
    
    def postRecord(self, record):
        rpcRecord = batcherrpc_pb2.RPCRecord(
            id = record.id,
            host = record.host,
            tags = record.tags,
            causality = batcherrpc_pb2.RPCCausality(
                host = record.prehost,
                toid = record.pretoid
            )
        )
        return self.stub.TOIDReceiveRecord(rpcRecord)

    def asyncPostRecord(self, record):
        rpcRecord = batcherrpc_pb2.RPCRecord(
            id = record.id,
            host = record.host,
            tags = record.tags,
            causality = batcherrpc_pb2.RPCCausality(
                host = record.prehost,
                toid = record.pretoid
            )
        )
        return self.stub.TOIDReceiveRecord.future(rpcRecord)

class Record:
    """Record consists of key-value pairs and casual dependency"""
    def __init__(self, id, host):
        self.id = id
        self.host = host
        self.tags = {}
        self.prehost = 0
        self.pretoid = 0

    def setParent(self, host, toid):
        self.prehost = host
        self.pretoid = toid

    def addTag(self, key, value):
        self.tags[key] = value
