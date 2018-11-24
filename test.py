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

def fale(texto):
    cmd_beg= 'espeak -vpt-br "'
    cmd_end= '" 2>/dev/null'
    call([cmd_beg+texto+cmd_end], shell=True)

def reconhecimento():
    print("Hello!")
    escreva("Reconhecimento")
    fale("Reconhecimento Iniciado")

button_one = Button(2)
button_two = Button(8)
button_tree = Button(7)

button_one.when_pressed = reconhecimento

pause()