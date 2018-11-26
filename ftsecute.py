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
from signal import pause
#Function falar palavras
def speakText(texto):
    cmd_beg= 'espeak -vpt-br "'
    cmd_end= '" 2>/dev/null'
    call([cmd_beg+texto+cmd_end], shell=True)
#Function falar palavras
def writeDisplay(texto):
    cmd_beg= 'python /home/pi/positivo-ft-secure/nokia.py "'
    cmd_end= '" 2>/dev/null'
    call([cmd_beg+texto+cmd_end], shell=True)
#Funcion reconhecimento
def reconhecimento():
      speakText("Reconhecimento Iniciado")
      #writeDisplay("Reconhecimento")

#Function treino
def treinar():
   var = 1
#Funcion capturar

def capturar():
   treinar()

def excluir():
   treinar()

writeDisplay("Bem Vindo")
speakText("Ola Seja bem vindo ao FT Secure")

button_one = Button(2)
button_two = Button(8)
button_tree = Button(7)

button_one.when_pressed = reconhecimento
button_two.when_pressed = capturar
button_tree.when_pressed = excluir
pause()
