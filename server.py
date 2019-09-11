import random
import argparse, socket
import os
import time
import sys
os.system("clear")
print "\033[91m"
print "################################"
print "################################"
print "################################"
print "################################"
print "\033[97m################################"
print "################################"
print "################################"
print "################################"
os.system("sleep 1")
os.system("toilet -f slant --gay Indonesia")
os.system("sleep 1")
print ("\033[96mANDAIKU BISA MENGHARUMKAN NAMA BANGSA INDONESIA")
os.system("sleep 1")
print ("\033[97m-Wahyudi Firmansyah-")
os.system("sleep 2")
os.system("clear")
os.system("sleep 1")
print "\033[91m"
print "          / /  ___   __ _(_)_ __     / __\ |__   __ _| |_" 
print "         / /  / _ \ / _` | | '_ \   / /  | '_ \ / _` | __|"
print "\033[97m        / /__| (_) | (_| | | | | | / /___| | | | (_| | |_" 
print "        \____/\___/ \__, |_|_| |_| \____/|_| |_|\__,_|\__|"
print "                    |___/"
print ""
os.system("sleep 1")
print "\033[96mCreated By: Wahyudi72 [ZxC7]"
os.system("sleep 1")
print "Support By: \033[91mGaruda Tersakti72"
def animasi(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
animasi("Selamat Datang di Server Chat ZxC7")
print ""
print "\033[93m===== ZxC7 Wahyudi72  ====="
print "\033[92m"
ip = raw_input("Ip addres: ")
port = input("Port     : ")
serverIP = ip
serverPort = 8080 
os.system("clear")
os.system("toilet -f standard --metal MyServer")
print "\033[91m"
print 'Server Pribadi ZxC7'
print 'Listening on : Tcp/Ip'
print 'ZxC7 (Garuda Tersakti72)'
print ''
listenerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #membuat object socket
listenerSocket.bind((serverIP,serverPort)) #binding socket
listenerSocket.listen(0) #listen socket
print ("\033[92mMenunggu Peka: ")
while True:
    handlerSocket, addr = listenerSocket.accept() #menerima ip dan port yang masuk
    print ('Server',addr,' Terhubung') #mencatat client yang masuk
    while True:
        message = handlerSocket.recv(1024) #menerima pesan yang masuk dari client
        print 'Pesan:',message
        message = raw_input("kamu : ") #inputan untuk mengetik pesan
        handlerSocket.send(message) #perintah mmengirim pesan
        pass
    pass
