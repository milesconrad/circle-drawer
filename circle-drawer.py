from pynput.mouse import Controller, Button
from math import cos, sin, radians
from time import sleep

sleep(3)
mouse = Controller()

for i in range(360 + 10):
    x = 960.5 + 400 * cos(radians(i))
    y = 520.5 + 400 * sin(radians(i))

    mouse.position = (x, y)
    if i == 0:
        mouse.press(Button.left)
    sleep(0.001)

mouse.release(Button.left)
