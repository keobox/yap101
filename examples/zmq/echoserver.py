import sys
import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
if len(sys.argv) == 1:
    port = 5000
else:
   port = int(sys.argv[1])
print "listening on port", port
socket.bind("tcp://127.0.0.1:%d" % port)
 
while True:
    msg = socket.recv()
    print "Got", msg
    socket.send(msg)
