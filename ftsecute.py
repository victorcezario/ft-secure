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
from espeak import espeak
espeak.set_voice("pt-br")

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
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((8,30), texto, font=font)
    disp.display()

writeDisplay("Cacique")
espeak.synth("Teste de Audio")

while espeak.is_playing:
	pass
print('Pressione Ctrl-C para sair.')
while True:
    time.sleep(1.0)
