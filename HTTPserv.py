#!/usr/bin/env python

'''
Adam Tigar and Meg Crenshaw
Threaded HTTP Server to handle GET/POST requests from a sensor

'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
from sys import argv

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>Initial response</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # Gets the size of data
        post_data = self.rfile.read(content_length) # Gets the data itself
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1><pre>" + post_data + "</pre></body></html>")
        
def run(server_class=ThreadingSimpleServer, handler_class=S, port=8080):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting http server on %s..'
    httpd.serve_forever()

if __name__ == "__main__":
    if len(argv) == 2:
        run(port=int(argv[1]))
        do_POST()
    else:
        run()
        do_POST()


