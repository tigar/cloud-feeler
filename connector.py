import http.client
import queue
import threading
import time
from sensor import Event

class eventQueueHandler:
    def __init__(self):
        eventQueue = queue.Queue()

class connection:
    def __init__(self):
        conn = http.client.HTTPConnection("localhost:8081")
        req = conn.request("POST", "/", "test")
        resp = conn.getresponse()
        print(resp)
