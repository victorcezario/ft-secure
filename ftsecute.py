# coding=utf-8

#ESPEAK


from gpiozero import Button
from signal import pause
from num2words import num2words
from subprocess import call
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

def reconhecimento():
      speakText("Reconhecimento Iniciado")
      writeDisplay("Reconhecimento")

writeDisplay("Bem Vindo")
speakText("Ola Seja bem vindo ao FT Secure")

button_one = Button(2)
button_two = Button(8)
button_tree = Button(7)

button_one.when_pressed = reconhecimento

pause()
