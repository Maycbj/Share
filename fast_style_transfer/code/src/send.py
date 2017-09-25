import socket
import cv2
import numpy

address = ('10.85.125.105', 8002)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(address)

capture = cv2.VideoCapture(0)
ret, frame = capture.read()
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
while ret:
    ret, frame = capture.read()
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR) 
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()
    sock.send( str(len(stringData)).ljust(16));
    sock.send( stringData );
    
sock.close()
cv2.destroyAllWindows()