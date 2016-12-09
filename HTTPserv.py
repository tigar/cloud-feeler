#!/usr/bin/env python

'''
Adam Tigar and Meg Crenshaw
Threaded HTTP Server to handle GET/POST requests from a sensor
'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import socketserver
from sys import argv

# Creates threads for each connection instance
class ThreadingSimpleServer(socketserver.ThreadingMixIn, HTTPServer):
    pass

class ServerRequestHandler(BaseHTTPRequestHandler):
    # Not used, initally for testing
    # Sends int response
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.wfile.write(bytes("<html><body><h1>Initial response</h1></body></html>", "utf8"))
        self.end_headers()

    def do_HEAD(self):
        self.send_response(202)
        self.end_headers()

    # Sends an int response
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        print(post_data)
        self.send_response(201)
        self.end_headers()

def run(server_class=ThreadingSimpleServer, handler_class=ServerRequestHandler, port=8080):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting http server on %s..' %port)
    httpd.serve_forever()

# Runs the server on port 8080 by default unless otherwise specified
if __name__ == "__main__":
    if len(argv) == 2:
        run(port=int(argv[1]))
        do_POST()
    else:
        run()
        do_POST()
