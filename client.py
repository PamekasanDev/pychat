import socket
import time
import os
import sys
os.system("clear")
os.system("toilet -f slant --gay LoginChat")
os.system("sleep 1")                                                  
print "\033[96mCreated By: Wahyudi72 [ZxC7]"
print "Support By: \033[91mGaruda Tersakti72" 
print ""
print "\033[93m===== Login Chat ======"
ip = raw_input("Ip address: ")
port = input("Port.         :")
serverIP = ip
serverPort = 8080
handlerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
handlerSocket.connect((serverIP,serverPort))
print ('Terhubung ke server ')
 
while True:
    message = raw_input("You : ")
    handlerSocket.send(message)
    message = handlerSocket.recv(1024)
    print 'pesan dari server : ',message
    pass
