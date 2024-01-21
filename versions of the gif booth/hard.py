#!/bin/sh
#import modules
import RPi.GPIO as GPIO
from time import sleep
import os
import picamera
from fractions import Fraction
from moviepy.editor import *
#export FFMPEG_BINARY=/usr/bin/ffmpeg
#import giphypop
from giphypop import upload
#from selenium import webdriver


import pygame
from pygame import *


#screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.init()


#create variables to hold commands 
makeVid = "convert -delay 50 image*.jpg animation.gif"
converti = "MP4Box -add video.h264 video.mp4"

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
        if(e.type is KEYDOWN and e.key == K_r):
            print('Button Pressed')
            sleep(0.2)

            img = pygame.image.load('jpgtitles/getready1.jpg')
            screen.blit(img,(0,0))
            pygame.display.flip()

            sleep(2)

            #img = pygame.image.load('jpgtitles/3.jpg')
            #screen.blit(img,(0,0))
            #pygame.display.flip()
            #sleep(1)
            #img = pygame.image.load('jpgtitles/2.jpg')
            #screen.blit(img,(0,0))
            #pygame.display.flip()
            #sleep(1)
            #img = pygame.image.load('jpgtitles/1.jpg')
            #screen.blit(img,(0,0))
            #pygame.display.flip()
            #sleep(1)
            

            #take 6 photos

            camera.start_preview()
            camera.start_recording('/home/pi/Desktop/video.h264')
            sleep(3)
            camera.stop_recording()
            camera.stop_preview()
            
            os.system(converti)
            #browser= webdriver.Chrome(executable_path='/path/to/chromedriver')
            #ffmpeg -i video.h264 -vcodec copy video.mp4
            #export FFMPEG_BINARY=/usr/bin/ffmpeg
            clip = (VideoFileClip("video.mp4").subclip((0,0.00),(0,3.00)))
                    #.resize(0.3)
            clip.write_gif("animation.gif")

            
            
            
            gif = upload(['#Cavea'], 'animation.gif', username='Cavea', api_key='R0Rz6Y5YYTgnRQ2DFlTf7r5obEqMzAml')
            print(gif) 


            print("uploaded")

#        GPIO.cleanup() #cleanup GPIO channels

#hit Ctrl + C to stop program
except KeyboardInterrupt:
    print ('program stopped')
