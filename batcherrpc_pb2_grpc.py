# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import batcherrpc_pb2 as batcherrpc__pb2


class BatcherRPCStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ReceiveRecord = channel.unary_unary(
        '/BatcherRPC/ReceiveRecord',
        request_serializer=batcherrpc__pb2.RPCRecord.SerializeToString,
        response_deserializer=batcherrpc__pb2.RPCReply.FromString,
        )
    self.ReceiveRecords = channel.unary_unary(
        '/BatcherRPC/ReceiveRecords',
        request_serializer=batcherrpc__pb2.RPCRecords.SerializeToString,
        response_deserializer=batcherrpc__pb2.RPCReply.FromString,
        )
    self.UpdateQueue = channel.unary_unary(
        '/BatcherRPC/UpdateQueue',
        request_serializer=batcherrpc__pb2.RPCQueues.SerializeToString,
        response_deserializer=batcherrpc__pb2.RPCReply.FromString,
        )
    self.TOIDReceiveRecord = channel.unary_unary(
        '/BatcherRPC/TOIDReceiveRecord',
        request_serializer=batcherrpc__pb2.RPCRecord.SerializeToString,
        response_deserializer=batcherrpc__pb2.RPCReply.FromString,
        )
    self.TOIDReceiveRecords = channel.unary_unary(
        '/BatcherRPC/TOIDReceiveRecords',
        request_serializer=batcherrpc__pb2.RPCRecords.SerializeToString,
        response_deserializer=batcherrpc__pb2.RPCReply.FromString,
        )
    self.TOIDUpdateQueue = channel.unary_unary(
        '/BatcherRPC/TOIDUpdateQueue',
        request_serializer=batcherrpc__pb2.RPCQueues.SerializeToString,
        response_deserializer=batcherrpc__pb2.RPCReply.FromString,
        )


class BatcherRPCServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ReceiveRecord(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReceiveRecords(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateQueue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TOIDReceiveRecord(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TOIDReceiveRecords(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TOIDUpdateQueue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BatcherRPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ReceiveRecord': grpc.unary_unary_rpc_method_handler(
          servicer.ReceiveRecord,
          request_deserializer=batcherrpc__pb2.RPCRecord.FromString,
          response_serializer=batcherrpc__pb2.RPCReply.SerializeToString,
      ),
      'ReceiveRecords': grpc.unary_unary_rpc_method_handler(
          servicer.ReceiveRecords,
          request_deserializer=batcherrpc__pb2.RPCRecords.FromString,
          response_serializer=batcherrpc__pb2.RPCReply.SerializeToString,
      ),
      'UpdateQueue': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateQueue,
          request_deserializer=batcherrpc__pb2.RPCQueues.FromString,
          response_serializer=batcherrpc__pb2.RPCReply.SerializeToString,
      ),
      'TOIDReceiveRecord': grpc.unary_unary_rpc_method_handler(
          servicer.TOIDReceiveRecord,
          request_deserializer=batcherrpc__pb2.RPCRecord.FromString,
          response_serializer=batcherrpc__pb2.RPCReply.SerializeToString,
      ),
      'TOIDReceiveRecords': grpc.unary_unary_rpc_method_handler(
          servicer.TOIDReceiveRecords,
          request_deserializer=batcherrpc__pb2.RPCRecords.FromString,
          response_serializer=batcherrpc__pb2.RPCReply.SerializeToString,
      ),
      'TOIDUpdateQueue': grpc.unary_unary_rpc_method_handler(
          servicer.TOIDUpdateQueue,
          request_deserializer=batcherrpc__pb2.RPCQueues.FromString,
          response_serializer=batcherrpc__pb2.RPCReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'BatcherRPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
