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
thread1 = Thread(chat)
thread2 = Thread(chatDisplay)
def chat():
    while Run:
        msg = input("Enter Text to send")
def chatDisplay():
    
    
    while Run:
        
        for event in pygame.event.get():#this is similiar to making a window in cpp events are like mouse clicks or keyboard presses they all get queued here
            if event.type == pygame.QUIT:#pygame.quit means the user hit the x button on the top right
                gameRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    isLeft = True
                if event.key == pygame.K_RIGHT:#keyup means the user lifted their finger off the key
                    isRight = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    isLeft = False
                if event.key == pygame.K_RIGHT:
                    isRight = False
        if(isLeft):
            x = x -1
        if(isRight):
            x = x + 1
        screen.fill((255,0,0))                   #these four numbers are left top width height
        pygame.draw.rect(screen, (255,255,255), [x,200,100,60],0)
        pygame.display.flip()# this flip is refering to how opengl(the low level language for your motherboard and shit) renders graphics it basically "flips" the image just know you need this to have the screen update
        clock.tick(24)#this is framerate
    pygame.quit()

    
