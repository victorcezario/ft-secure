# coding=utf-8
#Bibliotecas Nokia 5110
import time
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#Bibliotecas OpenCV
import cv2
import os
import glob

import faceDataset
import faceTraining
import faceRecognition

#LEDS
import RPi.GPIO as GPIO

#ESPEAK
from num2words import num2words
from subprocess import call

# Define Status dos botões
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-25
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-8
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-7

#Function escreve display
def writeDisplay(texto):
    # Raspberry Pi hardware SPI config:
    DC = 23
    RST = 24
    SPI_PORT = 0
    SPI_DEVICE = 0
    # Hardware SPI usage:
    disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

    # Initialize library.
    disp.begin(contrast=60)
    # Clear display.
    disp.clear()
    disp.display()
    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    # Draw a white filled box to clear the image.
    draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
    # Load default font.
    font = ImageFont.load_default()
    # Write some text.
    draw.text((2,10), texto, font=font)
    # Display image.
    disp.image(image)
    disp.display()

#Function falar palavras
def speakText(texto):
    cmd_beg= 'espeak -vpt-br "'
    cmd_end= '" 2>/dev/null'
    call([cmd_beg+texto+cmd_end], shell=True)

try:
    while True:
         button_one_state = GPIO.input(25)
         button_two_state = GPIO.input(8)
         button_tree_state = GPIO.input(7)

         #Ação do Botão 1
         if button_one_state == False or keyboard.is_pressed('1'):
            writeDisplay("FT SECURE")
            speakText("Ola Seja bem vindo ao FT Secure")
            faceRecognition.main()
            print('Pressione Ctrl-C para sair.')
            while True:
                time.sleep(1.0)
except:
    GPIO.cleanup()
