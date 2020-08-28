#!/usr/bin/env python
#
# set_frequency.py  - Einstellen der Frequenzsuche auf dem SP-H
#
#
import socket
import sys

def byteorder():
    return sys.byteorder

def standard_encoding():
    return sys.getdefaultencoding()

def standardausgabe_encoding():
    return sys.stdout.encoding

def string2bytes(text):
    return bytes(text, "utf8")

def bytes2string(bytes):
    return str(bytes, "utf8")

HOST = '172.10.10.1'  # Standard loopback interface address (localhost)
PORT = 1280        # Port to listen on (non-privileged ports are > 1023)
SERVER_ADDR = (HOST, PORT)

data = ""
rdata = ""


print ("\n set_frequenz.py - Folgende Werte sind möglich: \n\n")
print (" 800        - beschränkt die Suche auf die 800er Frequenz\n")
print (" 1800       - beschränkt die Suche auf die 1800er Frequenz\n")
print (" 2600       - beschränkt die Suche auf die 2600er Frequenz\n")
print (" 800-1800   - beschränkt die Suche auf die beiden Frequenzen 800, 1800\n")
print (" 1800-2600  - beschränkt die Suche auf die beiden Frequenzen 1800,2600\n")
print (" all        - aktiviert die Suche auf allen Frequenzen\n\n")
x = input("Bitte gewünschte Frequenz eingeben: ")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
 
    if x == '800': 
         data = 'at^syscfgex=\"03\",3FFFFFFF,3,1,80000,,\r'
         print ("\n 800 Frequenz wird aktiviert.\n")

    elif x == '1800': 
         data = 'at^syscfgex=\"03\",3FFFFFFF,3,1,4,,\r'
         print ("\n 1800 Frequenz wird aktiviert.\n")

    elif x == '2600':
         data = 'at^syscfgex=\"03\",3FFFFFFF,3,1,40,,\r'
         print ("\n 2600 Frequenz wird aktiviert.\n")
         
    elif x == '800+1800':
         data ='at^syscfgex=\"03\",3FFFFFFF,3,1,8004,,\r'
         print ("\n 800 und 1800 Frequenz wird aktiviert.\n")

    elif x == '1800+2600':
         data = 'at^syscfgex=\"03\",3FFFFFFF,3,1,44,,\r'
         print ("\n 1800 und 2600 Frequenz wird aktiviert.\n")

    elif x == 'all':
         data = 'at^syscfgex=\"03\",3FFFFFFF,3,1,80044,,\r'
         print ("\n Alle Bänder werden aktiviert.\n")

    else:
         print ("\n, x keine gültige Option\n")
         exit()

if data != "":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDR)
    client_socket.send(string2bytes(data)) 
    rdata = client_socket.recv(1024)
    rdatastring = bytes2string(rdata)
    print ("\n",rdatastring)
    client_socket.close()
    del client_socket
    