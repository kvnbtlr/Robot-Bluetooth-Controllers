import pygame, serial, sys
from pygame.locals import *

#Initialize pygame
pygame.init()
#Define serial port
ser = serial.Serial('/dev/tty.Bluetooth_Bee_V2-DevB', 9600)
clock = pygame.time.Clock()


class m3pi():
    def __init__(self):
        self.b_array = bytearray(1)
        self.b_array = [0]
    



def send_data():

    #Create robot object
    robot = m3pi()
   
    
    while 1:

        #Wait eighteen milliseconds each iteration
        pygame.time.delay(18)
        
        #Retrieve array of keys pressed
        keys = pygame.key.get_pressed()

        #Define arrow keys
        u = keys[K_UP]
        d = keys[K_DOWN]
        l = keys[K_LEFT]
        r = keys[K_RIGHT]
        plus = keys[K_EQUALS]
        minus = keys[K_MINUS]

        #Determine which combination of keys are pressed
        #Change byte array depending on what key is pressed
        if not u and not l and not r and not d: robot.b_array[0] = 0
        elif r and not u and not l and not d: robot.b_array[0] = 1
        elif l and not r and not u and not d: robot.b_array[0] = 2
        elif d and not u and not l and not r: robot.b_array[0] = 4
        elif d and r and not u and not l: robot.b_array[0] = 5
        elif d and l and not u and not r: robot.b_array[0] = 6
        elif u and not d and not l and not r: robot.b_array[0] = 8
        elif u and r and not d and not l: robot.b_array[0] = 9
        elif u and l and not r and not d: robot.b_array[0] = 10
        elif u and d and not r and not l: robot.b_array[0] = 12

        if plus: robot.b_array[0] = 13
        if minus: robot.b_array[0] = 14
        
        

        #Send byte array to the m3pi
        ser.write(robot.b_array)
       
        #Reinitialize the byte array
        robot.b_array = [0]
        pygame.event.pump()

send_data()
