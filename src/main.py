import numpy as np
import time
import signal
import sys

from joystick import Joystick
# from client.firasim import FIRASimCommand, FIRASimVision
from tools import speeds2motors, angError, norml, SpeedPair
from client.serialRadio import SerialRadio

js = Joystick()
serial = SerialRadio()
# vision = FIRASimVision('224.0.0.1', 10002)
# command = FIRASimCommand('127.0.0.1', 20011, team_yellow=False)

direction = 1
lastRefAngle = 0

def signal_handler(signal, frame):
    js.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def control(curAngle, refAngle, refVel, curVel, curW, turbo, spin, curBallVel):
    global lastRefAngle
    
    if turbo:
        w = 8 * angError(refAngle, curAngle)
        v = min(2, 7 / np.abs(curW))
    elif spin != 0:
        w = 60 * np.sign(spin)
        v = 0
    else:
        w = 9 * angError(refAngle, curAngle) + 0.01 * (refAngle - lastRefAngle) / 0.016
        v = refVel * 1#min(refVel * 1, 0.4 + (1 - 0.4) * np.exp(-1 * (curW+w)) )

    lastRefAngle = refAngle
    
    return speeds2motors(v * direction, w)

def optimalAngle(angle, direction):
    return angle + (np.pi if direction == -1 else 0)
    
t0 = 0
visionData = None

while True:

    refAngle = js.angle

    speed = js.speed
    w = js.w
    turbo = js.turbo
    spin = js.spin

    controlSpeed = [speed, w]
    speed = SpeedPair(*controlSpeed)
    serial.send([speed])

    #time.sleep(1 / 60.0)

    #print((time.time()-t0)*1000)

js.stop()
