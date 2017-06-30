import gochariots

seed = 9527

record = gochariots.Record(seed, 0)
record.add("key", "value")

gochariots.setHost("localhost:8080")
result = gochariots.post(record)

print(result.content)