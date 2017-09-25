import socket
import cv2
import numpy

fixed_size = 227

address = ('10.85.125.105', 8002)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(address)

capture = cv2.VideoCapture(0)
ret, frame = capture.read()
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
frame = cv2.resize(frame, (fixed_size,fixed_size), interpolation=cv2.INTER_LINEAR) 
while ret:
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()
    sock.send( str(len(stringData)).ljust(16));
    sock.send( stringData );
    ret, frame = capture.read()
    #frame = cv2.resize(frame, (fixed_size,fixed_size), interpolation=cv2.INTER_LINEAR) 
    frame = cv2.resize(frame, (0, 0), fx=0.6, fy=0.6, interpolation=cv2.INTER_LINEAR) 
    #decimg=cv2.imdecode(data,1)
    #cv2.imshow('CLIENT',decimg)

sock.close()
cv2.destroyAllWindows()