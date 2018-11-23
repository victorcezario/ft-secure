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
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-25
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-8
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-7

#Function escreve display
def writeDisplay(texto):
    # Raspberry Pi hardware SPI config:
    DC = 23
    RST = 24
    SPI_PORT = 0
    SPI_DEVICE = 0

    # Raspberry Pi software SPI config:
    # SCLK = 4
    # DIN = 17
    # DC = 23
    # RST = 24
    # CS = 8

    # Beaglebone Black hardware SPI config:
    # DC = 'P9_15'
    # RST = 'P9_12'
    # SPI_PORT = 1
    # SPI_DEVICE = 0

    # Beaglebone Black software SPI config:
    # DC = 'P9_15'
    # RST = 'P9_12'
    # SCLK = 'P8_7'
    # DIN = 'P8_9'
    # CS = 'P8_11'


    # Hardware SPI usage:
    disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

    # Software SPI usage (defaults to bit-bang SPI interface):
    #disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

    # Initialize library.
    disp.begin(contrast=60)

    # Clear display.
    disp.clear()
    disp.display()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a white filled box to clear the image.
    draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

    # Draw some shapes.
    draw.ellipse((2,2,22,22), outline=0, fill=255)
    draw.rectangle((24,2,44,22), outline=0, fill=255)
    draw.polygon([(46,22), (56,2), (66,22)], outline=0, fill=255)
    draw.line((68,22,81,2), fill=0)
    draw.line((68,2,81,22), fill=0)

    # Load default font.
    font = ImageFont.load_default()

    # Alternatively load a TTF font.
    # Some nice fonts to try: http://www.dafont.com/bitmap.php
    # font = ImageFont.truetype('Minecraftia.ttf', 8)

    # Write some text.
    draw.text((8,30), 'Hello World!', font=font)

    # Display image.
    disp.image(image)
    disp.display()

#Function falar palavras
def speakText(texto):
    cmd_beg= 'espeak -vpt-br "'
    cmd_end= '" 2>/dev/null'
    call([cmd_beg+texto+cmd_end], shell=True)

writeDisplay("FT SECURE")

try:
    while True:
         button_one_state = GPIO.input(2)
         button_two_state = GPIO.input(8)
         button_tree_state = GPIO.input(7)
         #Ação do Botão 1
         if button_one_state == False:
            writeDisplay("FT SECURE")
            speakText("Ola Seja bem vindo ao FT Secure")
            #faceRecognition.main()
            print('Pressione Ctrl-C para sair.')
         elif button_two_state == False:
            writeDisplay("FT SECURE")
            speakText("Ola Seja bem vindo ao FT Secure")
            #faceRecognition.main()
            print('Pressione Ctrl-C para sair.')
         elif button_tree_state == False:
            writeDisplay("FT SECURE")
            speakText("Ola Seja bem vindo ao FT Secure")
            #faceRecognition.main()
            print('Pressione Ctrl-C para sair.')
            
except:
    GPIO.cleanup()
