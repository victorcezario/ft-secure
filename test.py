# coding=utf-8
import sys
import time
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from gpiozero import Button
from signal import pause
from num2words import num2words
from subprocess import call

import faceDataset
import faceTraining
import faceRecognition


def escreva(texto):
    DC = 23
    RST = 24
    SPI_PORT = 0
    SPI_DEVICE = 0
    # Hardware SPI usage:
    disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))
    # Initialize library.
    disp.begin(contrast=90)
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
def imagem():
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

    # Load image and convert to 1 bit color.
    image = Image.open('capturar2.ppm').convert('1')

    # Alternatively load a different format image, resize it, and convert to 1 bit color.
    #image = Image.open('happycat.png').resize((LCD.LCDWIDTH, LCD.LCDHEIGHT), Image.ANTIALIAS).convert('1')

    # Display image.
    disp.image(image)
    disp.display()
def fale(texto):
    cmd_beg= 'espeak -vpt-br "'
    cmd_end= '" 2>/dev/null'
    call([cmd_beg+texto+cmd_end], shell=True)
def inicio():
    imagem()
def reconhecimento():
    #print("Hello!")
    escreva("RECONHECIMENTO")
    fale("Reconhecimento Iniciado")
    #faceDataset.main()
    #faceTraining.main()
    if(faceRecognition.main() == True):
        #fale("Face Encontrada")
        escreva("IDENTIFICADO")
        fale("Olá, tenha uma otima viagem, e digija, com cuidado !")
        call("omxplayer /home/pi/positivo-ft-secure/eurotrucker.mp3 2>/dev/null", shell=True)
        fale("Obrigado por viajar com a FT Secure")
        inicio()
    else:
        escreva("NAO ENCONTRADO")
        fale("Motorista não encontrado")
        inicio()
def cadastro():
    #call("rm -rf /home/pi/positivo-ft-secure/dataset/*")
    escreva("CADASTRO")
    fale("Cadastro Iniciado, por favor olhe para a camera")
    if(faceDataset.main() == True):
        fale("Cadastro Concluido")
        escreva("CADASTRO OK")
        fale("Iniciando Treinamento")
        escreva("TREINAMENTO")
        if(faceTraining.main() == True):
            fale("Treinamento Concluido")
            escreva("TREINAMENTO OK")
            inicio()
        else:
            fale("Erro no treinamento")
            escreva("TREINAMENTO ERROR")
    else:
        fale("Erro no cadastro")
        escreva("CADASTRO ERROR")
button_one = Button(2)
button_two = Button(3)
inicio()
fale("Bem Vindo ao FT SECURE")
button_one.when_pressed = reconhecimento
button_two.when_pressed = cadastro

pause()