import gochariots_client
import uuid

client = gochariots_client.RPCClient('localhost:9000')
record = gochariots_client.Record(str(uuid.uuid4()), 1, str(uuid.uuid4()))
record.addTag('k', 'v')

res = client.asyncPostRecord(record)
