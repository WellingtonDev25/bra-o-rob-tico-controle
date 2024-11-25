import cv2
import servo as serv
import json

with open("dados.json") as jsondados:
    dados = json.load(jsondados)

angBase = dados[0]["angInicial-base"]
angHorizontal = dados[0]["angInicial-horizontal"]
angVertical = dados[0]["angInicial-vertical"]
angGarra = dados[0]["angInicial-garra"]

def nothing(x):
    pass

cv2.namedWindow('controls')

cv2.createTrackbar('Base', 'controls', angBase, 180, nothing)
cv2.createTrackbar('Horizontal', 'controls', angHorizontal, 180, nothing)
cv2.createTrackbar('Vertical', 'controls',  angVertical, 180, nothing)
cv2.createTrackbar('Garra', 'controls',  angGarra, 180, nothing)

while True:
    try:
        # returns current position/value of trackbar
        base = int(cv2.getTrackbarPos('Base', 'controls'))
        hori = int(cv2.getTrackbarPos('Horizontal', 'controls'))
        vert = int(cv2.getTrackbarPos('Vertical', 'controls'))
        garra = int(cv2.getTrackbarPos('Garra', 'controls'))

        serv.mover(base,hori,vert,garra)

        if cv2.waitKey(1) ==27:
            break
    except:
        break

