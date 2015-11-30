import socket
import subprocess
__author__ = 'barin.huseyin'

#getting local ip address in python
print "Local ip address:",socket.gethostbyname(socket.gethostname())


#seeing activily listening ports
p=subprocess.Popen(["netstat -a -n -o"],shell=True,stdout=subprocess.PIPE)
out,err=p.communicate()

print out





mysocket=socket.socket()


try:
    print mysocket.connect(("192.168.40.1",139))
    print mysocket.send("GET / HTTP/1.0\n\n")
    print mysocket.recv(200)
except Exception as e:
    print e.args


print mysocket

print "Type:",type(mysocket)