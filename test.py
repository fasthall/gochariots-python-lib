import gochariots_client
import gochariots_toid_client
import uuid

client = gochariots_client.RPCClient('localhost:9000')
record = gochariots_client.Record(str(uuid.uuid4()), 1, str(uuid.uuid4()))
record.addTag('k', 'v')
res = client.asyncPostRecord(record)

toid_client = gochariots_toid_client.RPCClient('localhost:9000')
record = gochariots_toid_client.Record(str(uuid.uuid4()), 1)
record.addTag('k', 'v')
res = toid_client.asyncPostRecord(record)
