# coding=utf-8

#Bibliotecas OpenCV
import cv2
import os
import glob

import faceDataset
import faceTraining
import faceRecognition
#import nokia

#ESPEAK
from num2words import num2words
from subprocess import call

from gpiozero import Button
#Function falar palavras
def speakText(texto):
    cmd_beg= 'espeak -vpt-br "'
    cmd_end= '" 2>/dev/null'
    call([cmd_beg+texto+cmd_end], shell=True)

#nokia.writeDisplay("FT SECURE")
#Function falar palavras
def writeDisplay(texto):
    cmd_beg= 'python /home/pi/positivo-ft-secure/nokia.py "'
    cmd_end= '" 2>/dev/null'
    call([cmd_beg+texto+cmd_end], shell=True)

writeDisplay("Bem Vindo")
speakText("Ola Seja bem vindo ao FT Secure")
try:
    while True:
         button_one_state = Button(2)
         button_two_state = Button(8)
         button_tree_state = Button(7)
         #Ação do Botão 1
         if button_one_state.is_pressed:
            #nokia.writeDisplay("FT SECURE")
            speakText("Ola Seja bem vindo ao FT Secure")
            writeDisplay("FT Secure")
            #faceRecognition.main()
            print('Pressione Ctrl-C para sair.')
         elif button_two_state.is_pressed:
            #nokia.writeDisplay("FT SECURE")
            speakText("Ola Seja bem vindo ao FT Secure")
            #faceRecognition.main()
            print('Pressione Ctrl-C para sair.')
         elif button_tree_state.is_pressed:
            #nokia.writeDisplay("FT SECURE")
            speakText("Ola Seja bem vindo ao FT Secure")
            #faceRecognition.main()
            print('Pressione Ctrl-C para sair.')

