# coding=utf-8

#Bibliotecas OpenCV
import cv2
import os
import glob

import faceDataset
import faceTraining
import faceRecognition
import nokia
#LEDS
import RPi.GPIO as GPIO

#ESPEAK
from num2words import num2words
from subprocess import call

#GPIO.setmode(GPIO.BCM)
# Define Status dos botões
#GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-25
#GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-8
#GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-7

#Function falar palavras
def speakText(texto):
    cmd_beg= 'espeak -vpt-br "'
    cmd_end= '" 2>/dev/null'
    call([cmd_beg+texto+cmd_end], shell=True)

nokia.writeDisplay("FT SECURE")

try:
    while True:
         button_one_state = True: #GPIO.input(2)
         button_two_state = True: #GPIO.input(8)
         button_tree_state = True: #GPIO.input(7)
         #Ação do Botão 1
         if button_one_state == False:
            nokia.writeDisplay("FT SECURE")
            speakText("Ola Seja bem vindo ao FT Secure")
            #faceRecognition.main()
            print('Pressione Ctrl-C para sair.')
         elif button_two_state == False:
            nokia.writeDisplay("FT SECURE")
            speakText("Ola Seja bem vindo ao FT Secure")
            #faceRecognition.main()
            print('Pressione Ctrl-C para sair.')
         elif button_tree_state == False:
            nokia.writeDisplay("FT SECURE")
            speakText("Ola Seja bem vindo ao FT Secure")
            #faceRecognition.main()
            print('Pressione Ctrl-C para sair.')
            
except:
    GPIO.cleanup()
