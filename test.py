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
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-25