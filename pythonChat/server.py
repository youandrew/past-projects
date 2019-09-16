import socket
import threading

running = True
server = socket.socket()
server.bind("one on one", 7777)
server.listen(2)
client1 , client1Address = server.accept()
print("the first client has connected")
client1.send("welcome aboard client #1")
client2, client2Address = server.accept()
print("second client has connected")
client2.send("welcome client #2")
thread1 = Thread(listenClient, args = (client1))
thread2 = Thread(listenClient, args = (client2))
client1.send("type StopTalking exactly to end chat")
client2.send("type StopTalking exactly to end chat")
def listenClient(clientObj):
    while running:
        text = clientObj.recv(4028)
        if(text == "StopTalking"):
            client1.close()
            client2.close()
            client1.send("END CALL")
            client2.send("END CALL")
            running = false
        else:
            client1.send(text)
            client2.send(text)
