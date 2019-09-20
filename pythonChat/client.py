import socket
import pygame
import threading

Run = True
pygame.init()
size = (1600,900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pyChat")
clock = pygame.time.Clock()
player = socket.socket()
serverString = input("Enter name of host")
port = input("Enter port number")
player.connect(serverString,port)

textarray = []
font = pygame.font.Font("Arial",20)

thread1 = Thread(chat)
thread2 = Thread(chatDisplay)
thread3 = Thread(receive)

def recieve():
    while Run:
        text = player.recv(4028)
        textarray.append(text)
def chat():
    while Run:
        msg = input("Enter Text to send")
        player.send(msg)
def chatDisplay():
    
    
    while Run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRun = False
            
        screen.fill((255,0,0))
        y = 0
        for t in range(len(textarray)):
            text = font.render(textarray[t],True,(0,0,0))
            screen.blit(text,(0,y))
            y += 50
        pygame.display.flip()
        clock.tick(24)#this is framerate
    pygame.quit()
