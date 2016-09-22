import pygame, serial, sys
from get_stops import get_stops
from pygame.locals import *

#Initialize pygame
pygame.init()
#Define serial port
ser = serial.Serial('/dev/tty.Bluetooth_Bee_V2-DevB', 9600)
ser.timeout = 0 #Allows for pyserial to read info sent from m3pi
clock = pygame.time.Clock()

class m3pi():
    def __init__(self):
        self.b_array = bytearray(1)
        self.b_array = [0]
        
    


def send_data():
 
        
 
    
    robot = m3pi()
    seven_picked = False
    
    

    
    
    while not seven_picked:

        #Wait for twenty milliseconds each iteration
        pygame.time.delay(20)
        keys = pygame.key.get_pressed()
        
        #Retrieve array of keys pressed
        

        #Define keys to change speed
     
        one_s = keys[K_1]
        two_s = keys[K_2]
        three_s = keys[K_3]
        four_s = keys[K_4]
        five_s = keys[K_5]
        six_s = keys[K_6]
        seven_s = keys[K_7]
        

        
        

        #Determine which keys are pressed
        
            
            
        if one_s:
            robot.b_array[0] = 1
    
            
            print('1 selected \n')
            print(robot.b_array)
            ser.write(robot.b_array)
            
           
            
        elif two_s:
            
            robot.b_array[0] = 2
    
            
            print('2 selected \n')
            print(robot.b_array)
            ser.write(robot.b_array)
            
            
        elif three_s:
            
            robot.b_array[0] = 3
    
            
            print('3 selected \n')
            print(robot.b_array)
            ser.write(robot.b_array)
            
    
            
        elif four_s:
            
            robot.b_array[0] = 4
    
            
            print('4 selected \n')
            print(robot.b_array)
            ser.write(robot.b_array)
            
     
        
        elif five_s: 
            
            robot.b_array[0] = 5
    
            
            print('5 selected \n')
            print(robot.b_array)
            ser.write(robot.b_array)
            
       
            
        elif six_s:
            
            robot.b_array[0] = 6
    
            
            print('6 selected \n')
            print(robot.b_array)
            ser.write(robot.b_array)
            
           

        elif seven_s:
            print('7 selected')
            robot.b_array[0] = 7
            for x in range(0, 50):
                ser.write(robot.b_array)
            
            seven_picked = True
        else:
            robot.b_array[0] = 0
            ser.write(robot.b_array)
       
        line = ser.readline()
        #If the line isn't empty, print out the line
        #Used for printing time, constant, and speed to terminal
        if(line.decode("utf-8")  != ''):
            print(line.decode("utf-8"))

        line = None               
        
        
        
         
        

 
          
        
        pygame.event.pump()

    while 1:
        line = ser.readline()
        #If the line isn't empty, print out the line
        #Used for printing time, constant, and speed to terminal
        if(line.decode("utf-8")  != ''):
            print(line.decode("utf-8"))

        line = None
#Call function to send and receive data
send_data()

