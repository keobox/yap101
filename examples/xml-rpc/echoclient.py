
import xmlrpclib as xmlc

service = xmlc.ServerProxy('http://127.0.0.1:8001')
for i in range(10):
    msg = "msg %s" % i
    msg_in = service.echo(msg)
    print "Sending", msg, "received", msg_in
