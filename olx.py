#OPENCV
from imutils import paths
import cv2
import os
import glob

#LEDS
import RPi.GPIO as GPIO
import time
import keyboard

import capture
import recognition
import trainer

GPIO.setmode(GPIO.BCM)
# Define Status dos botões
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-25
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-8
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Botão GPIO-7

# Define posição dos leds
yellow = 20
red = 21
green = 16

# Define Status dos leds
GPIO.setup(red, GPIO.OUT)  #LED GPIO-21
GPIO.setup(yellow, GPIO.OUT)  #LED GPIO-20
GPIO.setup(green, GPIO.OUT)  #LED GPIO-16
GPIO.output(red, False)
GPIO.output(yellow, False)
GPIO.output(yellow, False)

def piscar_led(number):
     GPIO.output(number, True)
     time.sleep(0.2)
     GPIO.output(number, False)

# Inicia os leds ao executar o script
print("[INFO] Script Iniciado...\n")
GPIO.output(green, True)
time.sleep(1)
GPIO.output(green, False)
time.sleep(1)
GPIO.output(yellow, True)
time.sleep(1)
GPIO.output(yellow, False)
time.sleep(1)
GPIO.output(red, True)
time.sleep(1)
GPIO.output(red, False)
time.sleep(1)
print("[INFO] Aguardando comandos ...\n")

try:
    while True:
         button_one_state = GPIO.input(25)
         button_two_state = GPIO.input(8)
         button_tree_state = GPIO.input(7)

         #Ação do Botão 1
         if button_one_state == False or keyboard.is_pressed('1'):
                 print("[BUTTON] 1 Pressionado\n")
                 # Ascende o Led Amarelo
                 GPIO.output(yellow, True)
                 print("[ACTION] Iniciando Cadastro\n")
                 ret = capture.main()
                 trainer.main()
                 if(ret == True):
                     # Apaga o led Amarelo
                     GPIO.output(yellow, False)
                     # Ascende o led Verde
                     GPIO.output(green, True)
                     time.sleep(1)
                     # Apaga o led Verde
                     GPIO.output(green, False)
                     print("[REPLY] Cadastro Realizado com sucesso\n")
                 else:
                     # Apaga o led Amarelo
                     GPIO.output(yellow, False)
                     # Ascende o led Vermelho
                     GPIO.output(red, True)
                     time.sleep(1)
                     # Apaga o led Vermelho
                     GPIO.output(red, False)
                     print("[REPLY] Erro ao Realizar Cadastro\n")
         else:
             GPIO.output(yellow, False)

             #Ação do Botão 2
             if button_two_state == False or keyboard.is_pressed('2'):
                 print('[BUTTON] 2 Pressionado\n')
                 # Ascende o Led Amarelo
                 GPIO.output(yellow, True)
                 print("[ACTION] Iniciando Reconhecimento\n")
                 ret = recognition.main()
                 if(ret == True):
                    # Apaga o led Amarelo
                    GPIO.output(yellow, False)
                    # Ascende o led Verde
                    GPIO.output(green, True)
                    time.sleep(1)
                    # Apaga o led Verde
                    GPIO.output(green, False)
                    print("[REPLY] Reconhecimento Ok\n")
                 else:
                           # Apaga o led Amarelo
                           GPIO.output(yellow, False)
                           # Ascende o led Vermelho
                           GPIO.output(red, True)
                           time.sleep(1)
                           # Apaga o led Vermelho
                           GPIO.output(red, False)
                           print("[REPLY] Erro ao Reconhecimento\n")
             else:
                 GPIO.output(16, False)

                 #Ação do botão 3
                 if button_tree_state == False or keyboard.is_pressed('3'):
                     print('[BUTTON] 3 Pressionado\n')
                     # Ascende o Led Amarelo
                     GPIO.output(yellow, True)
                     print("[ACTION] Iniciando Limpeza\n")
                     ret = recognition.main()
                     if(ret == True):
                        files = glob.glob('Images/*')
                        for f in files:
                            os.remove(f)
                        file = glob.glob('Trainer/*')
                        for fu in file:
                            os.remove(fu)
                        # Apaga o led Amarelo
                        GPIO.output(yellow, False)
                        # Ascende o led Verde
                        GPIO.output(green, True)
                        time.sleep(1)
                        # Apaga o led Verde
                        GPIO.output(green, False)
                        print("[REPLY] Limpeza Realizada com sucesso\n")
                     else:
                            # Apaga o led Amarelo
                            GPIO.output(yellow, False)
                            # Ascende o led Vermelho
                            GPIO.output(red, True)
                            time.sleep(1)
                            # Apaga o led Vermelho
                            GPIO.output(red, False)
                            print("[REPLY] Erro ao Realizar Limpeza\n")

except:
    GPIO.cleanup()