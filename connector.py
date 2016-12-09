import http.client
import queue
import threading
import time
from sensor import Event

## Should hold a queue of Events that are sent to the server
## File is deleted if response is bad news

class eventQueueHandler:
    def __init__(self):
        eventQueue = queue.Queue()

class connection:
    def __init__(self):
        conn = http.client.HTTPConnection("localhost:8081")
        req = conn.request("POST", "/", "test")
        resp = conn.getresponse()
        print(resp)
