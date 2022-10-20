# coding: utf-8

import socket

hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))
myMessage="Salut, je suis le client ENSTA !"
socket.send(myMessage.encode("Utf8"))

print("Close")
socket.close()