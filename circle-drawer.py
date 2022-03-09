from pynput.mouse import Controller, Button
from math import cos, sin, radians
from time import sleep

sleep(3)
mouse = Controller()

for i in range(360 * 3 + 40):
    x = 960.5 + 400 * cos(radians(i / 3))
    y = 520.5 + 400 * sin(radians(i / 3))

    mouse.position = (x, y)
    if i == 0:
        mouse.press(Button.left)
    sleep(0.003)

mouse.release(Button.left)
