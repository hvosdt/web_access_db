import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '/Users/hvosdt/Ex/web_access_db/'
port = 8080

os.chdir(webdir)
srvraddr = ("", port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
