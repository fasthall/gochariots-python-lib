import requests
import json

host = ""

class Record:
    """Record consists of key-value pairs and casual dependency"""
    def __init__(self, seed, hash):
        self.tags = {}
        self.seed = seed
        self.hash = hash

    def add(self, key, value):
        self.tags[key] = value

    def toJSON(self):
        r = {"seed": self.seed, "prehash": self.hash, "tags": self.tags}
        return r

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