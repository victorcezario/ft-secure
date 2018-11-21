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


#Function escreve display
def writeDisplay(texto):
    # Raspberry Pi hardware SPI config:
    DC = 23
    RST = 24
    SPI_PORT = 0
    SPI_DEVICE = 0
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
    draw.text((8,30), texto, font=font)

    # Display image.
    disp.image(image)
    disp.display()

#Function falar palavras
def speakText(texto):
    cmd_beg= 'espeak -vpt-br "'
    cmd_end= '" 2>/dev/null'
    call([cmd_beg+texto+cmd_end], shell=True)

writeDisplay("Cacique")
speakText("Teste de Audio")

print('Pressione Ctrl-C para sair.')
while True:
    time.sleep(1.0)
