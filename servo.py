from pyfirmata import Arduino,SERVO
import time
import json

with open("dados.json") as jsondados:
    dados = json.load(jsondados)

portaCom = dados[0]["porta-com"]
pinBaseNum = dados[0]["pin-base"]
pinHorizontalNum = dados[0]["pin-horizontal"]
pinVerticalNum = dados[0]["pin-vertical"]
pinGarraNum = dados[0]["pin-garra"]

board = Arduino(portaCom)
pinBase = pinBaseNum
pinHorintal = pinHorizontalNum
pinVertical = pinVerticalNum
pinGarra = pinGarraNum

board.digital[pinBase].mode = SERVO
board.digital[pinHorintal].mode = SERVO
board.digital[pinVertical].mode = SERVO
board.digital[pinGarra].mode = SERVO

def rotateServo(pin,angle):
    board.digital[pin].write(angle)
    time.sleep(0.030)

atual5 = 0
atual6 = 0
atual7 = 0
atual8 = 0
numStep = 2

movimentos = []

def mover(val5, val6, val7, val8):
    global atual5
    global atual6
    global atual7
    global atual8

    # print('atual',atual5, atual6, atual7, atual8)
    # print('valor',val5, val6, val7, val8)

    if val5!=atual5:
        orientacao = numStep if val5 >= atual5 else (numStep-(numStep*2))
        print('orientacao val5',orientacao)
        if orientacao >=1:
            for x in range(atual5,val5,orientacao):
                rotateServo(pinBase,x)
        elif orientacao <0:
            print('orientacao negativa')
            for x in range(atual5,val5,orientacao):
                rotateServo(pinBase,x)

    if val6 != atual6:
        orientacao = numStep if val6 >= atual6 else (numStep-(numStep*2))
        print('orientacao val6', orientacao)
        if orientacao >=1:
            for x in range(atual6,val6,orientacao):
                rotateServo(pinHorintal,x)
        elif orientacao < 0:
            print('orientacao negativa')
            for x in range(atual6,val6,orientacao):
                rotateServo(pinHorintal,x)

    if val7 != atual7:
        orientacao = numStep if val7 >= atual7 else (numStep-(numStep*2))
        print('orientacao val7', orientacao)
        if orientacao >=1:
            for x in range(atual7,val7,orientacao):
                rotateServo(pinVertical,x)
        elif orientacao < 0:
            print('orientacao negativa')
            for x in range(atual7,val7,orientacao):
                rotateServo(pinVertical,x)

    if val8 != atual8:
        orientacao = numStep if val8 >= atual8 else (numStep-(numStep*2))
        print('orientacao val8', orientacao)
        if orientacao >=1:
            for x in range(atual8,val8,orientacao):
                rotateServo(pinGarra,x)
        elif orientacao <0:
            print('orientacao negativa')
            for x in range(atual8,val8,orientacao):
                rotateServo(pinGarra,x)

    atual5 = val5
    atual6 = val6
    atual7 = val7
    atual8 = val8


# print('passo1')
# mover(90,0,80,0)
# time.sleep(2)
# print('passo2')
# mover(90, 50, 100, 0)
# time.sleep(2)
# print('passo3')
# mover(0, 0, 0, 0)

