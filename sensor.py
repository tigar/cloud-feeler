import sys
import time
import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

maliciousFile = Path('evilFile')

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        what = 'directory' if event.is_directory else 'file'
        logging.info("Modified %s: %s", what, event.src_path)

    def on_created(self, event):
        what = 'directory' if event.is_directory else 'file'
        logging.info("Created %s: %s", what, event.src_path)

def startLogging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_object = FileSystemEventHandler()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
            if not maliciousFile.exists():
                observer.stop()
                break
    except KeyboardInterrupt:
        observer.stop()
        return 1
    observer.join()
    return 0

if __name__ == "__main__":
    try:
        while True:
            time.sleep(1)
            if maliciousFile.exists():
                if startLogging() == 1:
                    break
    except KeyboardInterrupt:
        pass