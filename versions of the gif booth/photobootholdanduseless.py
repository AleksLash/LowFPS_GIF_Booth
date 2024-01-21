#import modules
import RPi.GPIO as GPIO
from time import sleep
import os
import picamera
from fractions import Fraction

#import giphypop
from giphypop import upload

import pygame
from pygame import *


screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)

pygame.display.init()


#create variables to hold commands 
makeVid = "convert -delay 50 image*.jpg animation.gif"


#create variables to hold pin numbers
button = 18


#set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



camera = picamera.PiCamera() #initiate picamera module and class
camera.resolution = (1366, 768) #set resolution of picture here
camera.brightness = 60 #set brightness settings to help with dark photos
camera.annotate_foreground = picamera.Color(y=0.2, u=0, v=0) #set color of annotation 





try:
    #read button 
    while True:

        img = pygame.image.load('jpgtitles/title.jpg')
        screen.blit(img,(0,0))
        pygame.display.flip()
        
        for e in pygame.event.get():
            if(e.type is KEYDOWN and e.key == K_q):
                if screen.get_flags() & FULLSCREEN:
                    pygame.quit()
                    quit()

        
        #input_state = GPIO.input(button)
        #if input_state == True:
        #for e in pygame.event.get():
            elif(e.type is KEYDOWN and e.key == K_r):
                print('Button Pressed')
                sleep(0.2)
    
                img = pygame.image.load('jpgtitles/getready1.jpg')
                screen.blit(img,(0,0))
                pygame.display.flip()
    
                sleep(2)

                img = pygame.image.load('jpgtitles/3.jpg')
                screen.blit(img,(0,0))
                pygame.display.flip()
                sleep(1)
                img = pygame.image.load('jpgtitles/2.jpg')
                screen.blit(img,(0,0))
                pygame.display.flip()
                sleep(1)
                img = pygame.image.load('jpgtitles/1.jpg')
                screen.blit(img,(0,0))
                pygame.display.flip()
                sleep(1)
            

            #take 6 photos

                for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):

                    img = pygame.image.load('image0%s.jpg' %(i+1))
                    screen.blit(img,(0,0))
                    pygame.display.flip()
                    sleep(0.00005)

                    if i == 5:
                        img = pygame.image.load('jpgtitles/uploading.jpg')
                        screen.blit(img,(0,0))
                        pygame.display.flip()
                        break
                
                    img = pygame.image.load('jpgtitles/3.jpg')
                    screen.blit(img,(0,0))
                    pygame.display.flip()                
                
                
                    sleep(1)
                    img = pygame.image.load('jpgtitles/2.jpg')
                    screen.blit(img,(0,0))
                    pygame.display.flip()
                    sleep(1)
                    img = pygame.image.load('jpgtitles/1.jpg')
                    screen.blit(img,(0,0))
                    pygame.display.flip()
                    sleep(1)



                os.system(makeVid) #send command to convert images to GIF
                print('uploading') #let us know photo is about to start uploading


#
#           IN THE LINE BELOW YOU MUST INSERT CUSTOM TAGS, YOUR USERNAME AND YOUR GIPHY API KEY
#

                gif = upload(['*****INSERT CUSTOM TAGS*****'], 'animation.gif', username='Cavea', api_key='R0Rz6Y5YYTgnRQ2DFlTf7r5obEqMzAml')
                gif 


                print("uploaded") #let us know GIF has been uploaded
            
                i = 0
                z = 0
                while (i < 5):

                    if z== 6:
                        break
                
                    img = pygame.image.load('image0%s.jpg' %(i+1))
                    screen.blit(img,(0,0))
                    pygame.display.flip()
                    sleep(0.2)
    
                    for e in pygame.event.get():
                        if(e.type is KEYDOWN and e.key == K_q):
                            if screen.get_flags() & FULLSCREEN:
                                pygame.quit()
                                quit()
    
                    i += 1
    
                    if i==5:
                        z += 1
                        i=0
                    
#        GPIO.cleanup() #cleanup GPIO channels

#hit Ctrl + C to stop program
except KeyboardInterrupt:
    print ('program stopped')
