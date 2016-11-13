import Flask.alarmservice as AlarmService
from gpiozero import MotionSensor
import subprocess
import datetime
import RPi.GPIO as GPIO
import time

# Definiciones
red_PIN = 16
pir = MotionSensor(17)
buzz_PIN = 26
# green_PIN = XX
MAIN_PATH = "/home/pi/PiSec"

# Seteos
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzz_PIN, GPIO.OUT)
## Los leds se usan de la siguiente forma:
## - Verde: alarma desactivada
## - Rojo: movimiento detectado
## - Apagados: alarma encendida

GPIO.setup(red_PIN, GPIO.OUT)
# GPIO.setup(green_PIN, GPIO.OUT)

# Comienzo de PiSec
print ("PIR Module Test (CTRL+C to exit)")
time.sleep(2)
print ("Ready")
n = 0
status = 0  # El sistema inicia desactivado

# Verifica la excepcion de teclado para poder salir.
try:
    while True:
        if pir.motion_detected:
            print("Motion detected!")
            time.sleep(0.3)
            print("Taking picture!")
            AlarmService.take_picture_auto()
            print("Done!")


except KeyboardInterrupt:
    print ("Quit")
