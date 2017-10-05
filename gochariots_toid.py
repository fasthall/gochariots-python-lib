import requests
import json

host = ""

class Record:
    """Record consists of key-value pairs and casual dependency"""
    def __init__(self, id):
        self.id = id
        self.tags = {}
        self.prehost = 0
        self.pretoid = 0

    def setDependency(self, prehost, pretoid):
        self.prehost = prehost
        self.pretoid = pretoid

    def add(self, key, value):
        self.tags[key] = value

    def toJSON(self):
        r = {"id": self.id, "prehost": self.prehost, "pretoid": self.pretoid, "tags": self.tags}
        return r

class Result:
    def __init__(self, lid, toid, host):
        self.LId = lid
        self.TOId = toid
        self.Host = host

def setHost(_host):
    global host
    if not _host.startswith("http://"):
        _host = "http://" + _host
    host = _host

def post(record):
    if host == "":
        print("Host not set yet")
        return
    return requests.post(host + "/record", json = record.toJSON())

def get(id, timeout=10):
    response = requests.get(host + "/record/" + str(id) + "?timeout=" + str(timeout))
    if response.status_code == 200:
        result = json.loads(response.text)
        return Result(result['LId'], result['TOId'], result['Host'])
    else:
        return None