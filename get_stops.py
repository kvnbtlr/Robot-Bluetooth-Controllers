import pygame, serial, sys
from pygame.locals import *

def get_stops():
    not_picked = True
    stops = 0
    print('How many stops would you like to take: \n')
    while not_picked:

        pygame.time.delay(20)
        keys = pygame.key.get_pressed()

        #Define keys to change speed
        
        two_s = keys[K_2]
        three_s = keys[K_3]
        four_s = keys[K_4]
        five_s = keys[K_5]
        six_s = keys[K_6]
         
        eight_s = keys[K_8]
        
        ten_s = keys[K_0]
        ten_s = keys[K_0]
         
        if two_s:
            stops = 2
    
            not_picked = False
            print('2 stops selected \n')
            pygame.time.delay(500)
        elif three_s:
            stops = 3
            not_picked = False
            print('3 stops selected \n')
            pygame.time.delay(500)
            
        elif four_s:
            
            stops = 4
            not_picked = False
            print('4 stops selected \n')
            pygame.time.delay(500)
        elif five_s:
            stops = 5
            not_picked = False
            print('5 stops selected \n')
            pygame.time.delay(500)
            
        elif six_s:
            
            stops = 6
            not_picked = False
            print('6 stops selected \n')
            pygame.time.delay(500)
            
        elif eight_s:
            
            stops = 8
            not_picked = False
            print('8 stops selected \n')
            pygame.time.delay(500)
        elif ten_s:
            stops = 10
            not_picked = False
            print('10 stops selected \n')
            pygame.time.delay(500)
        
        
        pygame.event.pump()
        
    return stops
