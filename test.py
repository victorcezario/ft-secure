from gpiozero import Button
from signal import pause
from num2words import num2words
from subprocess import call

def writeDisplay(texto):
    cmd_beg= 'python /home/pi/positivo-ft-secure/nokia.py "'
    cmd_end= '" 2>/dev/null'
    call([cmd_beg+texto+cmd_end], shell=True)

def say_hello():
    print("Hello!")
    writeDisplay("xxxxxxxxx")
button = Button(2)

button.when_pressed = say_hello

pause()