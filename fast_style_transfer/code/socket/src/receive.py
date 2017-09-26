import socket
import cv2
import numpy

address = ('10.236.10.44', 8003)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(True)

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

conn, addr = s.accept()
while True:
    length = recvall(conn,16)
    stringData = recvall(conn, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')
    decimg=cv2.imdecode(data,1)
    #decimg = cv2.resize(decimg, (640,640), interpolation=cv2.INTER_LINEAR) 
    #decimg = cv2.resize(decimg, (1280, 720), interpolation=cv2.INTER_LINEAR) 
    cv2.imshow('Style-Transfer',decimg)
    print decimg.shape
    cv2.waitKey(1)
    #if cv2.waitKey(10) == 27:
    #   break
    
s.close()
cv2.destroyAllWindows()