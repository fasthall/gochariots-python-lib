import gochariots

seed = 9527
gochariots.setHost("localhost:8080")

r1 = gochariots.Record(seed)
r1.add("first", "event")

r2 = gochariots.Record(seed)
r2.add("second", "event")
r2.setHash(gochariots.getHash(r1)[0])

result = gochariots.post(r2)
print(result.content)
result = gochariots.post(r1)
print(result.content)