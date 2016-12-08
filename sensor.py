#!/usr/bin/env python3

'''
Adam Tigar and Meg Crenshaw
Sensor to send activity to server, read response,
and delete malicious files
'''

import sys
import time
import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
import http.client

maliciousFileString = 'evilFile'

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        what = 'directory' if event.is_directory else 'file'
        logging.info("Modified %s: %s", what, event.src_path)
        conn = http.client.HTTPConnection("localhost:8081")
        req = conn.request("POST", "/", "modified")
        resp = conn.getresponse()
        print(resp.status)

    def on_created(self, event):
        what = 'directory' if event.is_directory else 'file'
        logging.info("Created %s: %s", what, event.src_path)
        conn = http.client.HTTPConnection("localhost:8081")
        req = conn.request("POST", "/", "created")
        resp = conn.getresponse()
        print(resp.status)

def startLogging(path):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_object = FileSystemEventHandler()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
            if not Path(path+maliciousFileString).exists():
                observer.stop()
                break
    except KeyboardInterrupt:
        observer.stop()
        return 1
    observer.join()
    return 0

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    try:
        while True:
            time.sleep(1)
            if Path(path+maliciousFileString).exists():
                if startLogging(path) == 1:
                    break
    except KeyboardInterrupt:
        pass
