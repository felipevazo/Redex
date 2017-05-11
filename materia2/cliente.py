import socket()
s=socket.socket()
s.connect(('127.0.0.1',9999))
while True:
    msg = raw_input('>>> ') # metodo que lee hasta que el usuario apreta enter
    s.send(msg)
    if msg == "quit":
        break
print "shao loh vimoh"
s.close()    
