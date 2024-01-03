from pyfirmata import Arduino
import time


board = Arduino('COM6') #change to the specific COM port of your connection
pin13 = board.get_pin('d:13:o')

def lightOn():
    pin13.write(1)
    time.sleep(0)

def lightOff():
    pin13.write(0)
    time.sleep(3)

while (True):
    direction = input("What direction do you want to go?\n")

    if(direction == 'forward'):
        lightOn()
    elif(direction == 'stop'):
        lightOff()