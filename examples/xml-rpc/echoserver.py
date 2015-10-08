import SimpleXMLRPCServer as xmls

def echo(msg):
    print 'Got', msg
    return msg

class echoserver(xmls.SimpleXMLRPCServer):
    allow_reuse_address = True

server = echoserver(('127.0.0.1', 8001))
server.register_function(echo, 'echo')
print 'Listening on port 8001'
try:
    server.serve_forever()
except:
    server.server_close()
