import pygame, serial, sys
from pygame.locals import *

#Initialize pygame
pygame.init()
#Define serial port
ser = serial.Serial('/dev/tty.Bluetooth_Bee_V2-DevB', 9600)
ser.timeout = 0 #Allows for pyserial to read info sent from m3pi
clock = pygame.time.Clock()

class m3pi():
    def __init__(self):
        self.b_array = bytearray(2)
    



def send_data():

    #Create robot object
    robot = m3pi()
    #Initialize byte array
    robot.b_array[0] = 10
    robot.b_array[1] = 10
    
    while 1:

        #Wait for twenty milliseconds each iteration
        pygame.time.delay(20)
        
        #Retrieve array of keys pressed
        keys = pygame.key.get_pressed()

        #Define keys to change speed
        zero_s = keys[K_0] and keys[K_s]
        one_s = keys[K_1] and keys[K_s]
        two_s = keys[K_2] and keys[K_s]
        three_s = keys[K_3] and keys[K_s]
        four_s = keys[K_4] and keys[K_s]
        five_s = keys[K_5] and keys[K_s]
        six_s = keys[K_6] and keys[K_s]
        seven_s = keys[K_7] and keys[K_s]
        eight_s = keys[K_8] and keys[K_s]
        nine_s = keys[K_9] and keys[K_s]

        #Define keys to change K constant
        zero_k = keys[K_0] and keys[K_k]
        one_k = keys[K_1] and keys[K_k]
        two_k = keys[K_2] and keys[K_k]
        three_k = keys[K_3] and keys[K_k]
        four_k = keys[K_4] and keys[K_k]
        five_k = keys[K_5] and keys[K_k]
        six_k = keys[K_6] and keys[K_k]
        seven_k = keys[K_7] and keys[K_k]
        eight_k = keys[K_8] and keys[K_k]
        nine_k = keys[K_9] and keys[K_k]

        #Determine which keys are pressed
        if zero_s: robot.b_array[0] = 0
        elif one_s: robot.b_array[0] = 1
        elif two_s: robot.b_array[0] = 2
        elif three_s: robot.b_array[0] = 3
        elif four_s: robot.b_array[0] = 4
        elif five_s: robot.b_array[0] = 5
        elif six_s: robot.b_array[0] = 6
        elif seven_s: robot.b_array[0] = 7
        elif eight_s: robot.b_array[0] = 8
        elif nine_s: robot.b_array[0] = 9
        elif zero_k: robot.b_array[1] = 0
        elif one_k: robot.b_array[1] = 1
        elif two_k: robot.b_array[1] = 2
        elif three_k: robot.b_array[1] = 3
        elif four_k: robot.b_array[1] = 4
        elif five_k: robot.b_array[1] = 5
        elif six_k: robot.b_array[1] = 6
        elif seven_k: robot.b_array[1] = 7
        elif eight_k: robot.b_array[1] = 8
        elif nine_k: robot.b_array[1] = 9
        
        
        #Write byte array to m3pi
        ser.write(robot.b_array)
        #Read information sent from m3pi
        line = ser.readline()
        #If the line isn't empty, print out the line
        #Used for printing time, constant, and speed to terminal
        if(line.decode("utf-8")  != ''):
            print(line.decode("utf-8"))

        line = None
        
        robot.b_array[0] = 10
        robot.b_array[1] = 10
        pygame.event.pump()

#Call function to send and receive data
send_data()

